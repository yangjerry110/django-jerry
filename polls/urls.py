from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    #详情
    path('<int:question_id>/',views.detail,name='detail'),
    #result
    path('<int:question_id>/results/',views.results,name="results"),
    #vote
    path('<int:question_id>/vote/',views.vote,name="vote"),
    #问题列表
    path('fivList',views.fiveQuestion,name='fiveQuestion'),
    #设置爬取参数页面
    path('setHtmlInfo',views.setHtmlInfo,name="setHtmlInfo"),
    #获取爬取参数页面
    path('getHtmlInfo',views.getHtmlInfo,name="getHtmlInfo")
]