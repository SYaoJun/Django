## Django实战
- 一个简单的server，界面看起来还可以。
## 书籍
- 《跟老齐学Python:Django实战》
## 视频
- [B站米修](https://www.bilibili.com/video/BV1KJ41117HL?p=15)
## settings
- interpreter
- package
## environment
```shell
python3 --version
- Python 3.9.6
django-admin --version
- 4.1.3
```
## starter
```shell
# 创建项目
django-admin startproject my_project_name
# 创建app
python3 manage.py runserver 0.0.0.0:8000
# 启动server
```
## 注意点
- 不能再用path做路由，必须要使用re_path