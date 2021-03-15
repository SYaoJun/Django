from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    # 上传文件
    path('upload_file/', views.upload_file),
    # ajax请求数据
    path('login/', views.login),
    path('login_ajax/', views.login_ajax),
]
