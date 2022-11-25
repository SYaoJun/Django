from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^hello', views.hello),
    re_path('', views.home, name='home'),
    re_path('user/', views.user, name='user'),
    # 上传文件
    re_path('upload_file/', views.upload_file),
    # ajax请求数据
    re_path('login/', views.login),
    re_path('login_ajax/', views.login_ajax),
]