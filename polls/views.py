from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
import pdb
from selenium import webdriver
from polls.webdriverDiy import webdriverDiySet

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
    title = request.POST['title']
    #pdb.set_trace() # 运行到这里会自动暂停
    result = webdriverDiySet(url,title)
    #pdb.set_trace() # 运行到这里会自动暂停
    return HttpResponse('返回的json：<br/> %s ' % result)
