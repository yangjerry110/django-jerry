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
    path('getHtmlInfo',views.getHtmlInfo,name="getHtmlInfo"),
    #测试获取配置文件
    path('testReadConf',views.testReadConf,name="testReadConf"),
    #上传文件展示页面
    path('fileUpload',views.fileUpload,name="fileUpload"),
    #上传文件提交
    path('fileUploadPost',views.fileUploadPost,name="fileUploadPost"),
    #上传文件列表
    path('fileUserList',views.fileUserList,name="fileUserList"),
    #点击详情，执行conf
    path('fileUserAction/<int:file_user_id>',views.fileUserAction,name="fileUserAction"),
    #path('fileReadForDecode',views.fileReadForDecode,name="fileReadForDecode"),
    #外部调用，自定义配置
    path('confDiy',views.confDiy,name="confDiy"),
    #测试json模板的数据渲染
    path('testJson',views.testJson,name="testJson")
]