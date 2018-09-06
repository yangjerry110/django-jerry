# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import pdb
import json
import leancloud

def webdriverDiySet(url,params):
    driver = webdriver.Chrome()
    driver.get(url)
    returnArray = []

    for i in params:
        #jsParams = 'return %s ' % i
        returnArray.append({i:driver.execute_script(params[i])})

    driver.quit()
    return json.dumps(returnArray)

#获取列表
def webdriverDiySetForConfig(data):
    resultData = {}
    #读详细配置
    #pdb.set_trace() # 运行到这里会自动暂停
    try:
        driver = webdriver.Chrome()
        #循环url
        for i in data['url']:
            #此处单独定义返回key内容
            returnData = {}
            driver.get(i)
            #循环获取params里面，并且执行js
            for x in data['params']:
                returnData[x] = driver.execute_script(data['params'][x])
            resultData[i] = returnData
            
        #pdb.set_trace() # 运行到这里会自动暂停
        #插入数据库
        if data['save']:
            if data['database_driver'] == 'leancloud':
                sendData = {"table":data['table'],"data":resultData,"type":"insert"}
                #pdb.set_trace() # 运行到这里会自动暂停
                leanCloudFunction(sendData)

        # driver.get(data['url'])
        # #pdb.set_trace() # 运行到这里会自动暂停
        # #获取列表conf加载之后，获取的详情urls
        # urls = driver.execute_script(data['data'])
        # #pdb.set_trace() # 运行到这里会自动暂停
        # for i in urls:
        #     driver.get(i)
        #     for x in data['params']:
        #         returnJson = {x:driver.execute_script(data['params'][x])}
        #     #获取详情
        #     #pdb.set_trace() # 运行到这里会自动暂停
        #     resultData.append(returnJson)

        # #插入数据库
        # if data['save']:
        #     if data['database_driver'] == 'leancloud':
        #         sendData = {"table":data['table'],"data":resultData,"type":"insert"}
        #         #pdb.set_trace() # 运行到这里会自动暂停
        #         leanCloudFunction(sendData)

    #判断参数异常 
    except KeyError as e:
        return json.dumps({'error':'1','data':"缺少参数 %s " % e})   
    driver.quit()
    return json.dumps({'error':0,'data':resultData})

def leanCloudFunction(data):
    appId = 'DGQowA9d1KJtUlORL3OgSgSc-gzGzoHsz'
    appKey = 'uHBjnX6lQIbTQQnfuJg42JvU'
    leancloud.init(appId,appKey)
    if data['type'] == 'insert':
        leanCloudInsert(data)
    return True

def leanCloudInsert(data):
    for i in data['data']:
        thisObj = leancloud.Object.extend(data['table'])
        this_Obj = thisObj()
        for x in data['data'][i]:
            this_Obj.set(x,data['data'][i][x])
        this_Obj.save()
    return True