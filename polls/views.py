from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,fileUser
from django.template import loader
import pdb
from selenium import webdriver
from polls.webdriverDiy import webdriverDiySet,webdriverDiySetForConfig
import json
import os,sys

# Create your views here.

def index(request):
    return HttpResponse("Hello people welcome to django")

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    try:
        #quetionInfo = models.Question.objects.get(pk=question_id)
        quetionInfo = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does note exist")
    return render(request,'polls/detail.html',{'quetionInfo':quetionInfo})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def fiveQuestion(request):
    five_question_list = Question.objects.order_by('-pud_data')[:5]
    pdb.set_trace() # 运行到这里会自动暂停
    template = loader.get_template('polls/index.html')
    context = {
        'five_question_list': five_question_list,
    }
    #最标准的写法
    return HttpResponse(template.render(context, request))
    #还有一种快捷的写法
    #return render(request,'polls/index.html',context)

def setHtmlInfo(request):
    return render(request,'polls/setHtmlInfo.html')

def getHtmlInfo(request):
    url = request.POST['url']
    params = request.POST.getlist('')
    #pdb.set_trace() # 运行到这里会自动暂停
    result = webdriverDiySet(url,params)
    #pdb.set_trace() # 运行到这里会自动暂停
    return HttpResponse('返回的json：<br/> %s ' % result)

def testReadConf(request):
    #return HttpResponse("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
    f = open('polls/conf/test.json','r')
    jsonInfo = json.load(f)
    result = webdriverDiySetForConfig(jsonInfo)
    #pdb.set_trace() # 运行到这里会自动暂停
    return HttpResponse(result)

def testReadConfInfo(request):
    f = open('polls/conf/test_info.json','r')
    jsonInfo = json.load(f)
    result = webdriverDiySetForConfigInfo(jsonInfo)

def fileUpload(request):
    return render(request,'polls/fileUpload.html')

def fileUploadPost(request):
    obj = request.FILES.get('file')
    f = open(os.path.join("D:\wnmp\www\coding\meilimei\django-jerry\polls\static",obj.name), 'wb')
    #插入数据库  - sqliate
    fileModel = fileUser(file_name="D:/wnmp/www/coding/meilimei/django-jerry/polls/static/"+str(obj.name))
    fileModel.save()

    for chunk in obj.chunks():
        f.write(chunk)
    f.close()
    return HttpResponseRedirect('/polls/fileUserList')
    #return  HttpResponse('OK')

def fileUserList(request):
    fileUserList = fileUser.objects.all()
    template = loader.get_template('polls/fileUserList.html')
    context = {
        'fileUserList': fileUserList,
    }
    #最标准的写法
    #return HttpResponse(template.render(context, request))
    #还有一种快捷的写法
    return render(request,'polls/fileUserList.html',context)

def fileUserAction(request,file_user_id):
    try:
        fileUserInfo = fileUser.objects.get(pk=file_user_id)
    except fileUser.DoesNotExist:
        raise Http404("fileUser does note exist")
    #pdb.set_trace() # 运行到这里会自动暂停
    #执行配置    
    f = open(fileUserInfo.file_name,'r')
    jsonInfo = json.load(f)
    result = webdriverDiySetForConfig(jsonInfo)
    #pdb.set_trace() # 运行到这里会自动暂停
    return HttpResponse(result)

#从外部调用我们的方法，自定义参数
def confDiy(request):
    #return HttpResponse('ok')
    if request.method == 'POST':
        receiveData = json.loads(request.body)
        #pdb.set_trace() # 运行到这里会自动暂停
        try:
            if 'fileUserId' in receiveData:
                fileUserInfo = fileUser.objects.get(pk=receiveData['fileUserId'])
                f = open(fileUserInfo.file_name,'r')
                jsonInfo = json.load(f)
                for i in receiveData:
                    jsonInfo[i] = receiveData[i]
            else:
                jsonInfo = receiveData

            #pdb.set_trace() # 运行到这里会自动暂停
            result = webdriverDiySetForConfig(jsonInfo)
            #pdb.set_trace() # 运行到这里会自动暂停
            return HttpResponse(result)
        except Exception as e:
            returnData = {'error':1,'data':'error: %s ' %e}
    else:
        returnData = {'error':1,'data':'method error'}
    
    returnJson = json.dumps(returnData)    
    return HttpResponse(returnJson)

    
