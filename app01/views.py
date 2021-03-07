from django.shortcuts import render
import requests
import json

def home(request):
    api_json = requests.get('https://api.github.com/users?since=0')
    api = json.loads(api_json.content)
    return render(request, 'home.html', {"api": api})
    #render用来打开html文件，对文件进行渲染。交给wsgi中的socket

def user(request):
    if request.method == 'POST':
        user = request.POST['user']
        user_request = requests.get('https://api.github.com/users/' + user)
        user_name = json.loads(user_request.content)
        return render(request, 'user.html', {'user': user, 'user_name': user_name})
    else:
        not_found = "请在搜索框输入您要查询的用户..."
        return render(request, 'user.html', {'not_found': not_found})

