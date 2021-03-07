

from django.contrib import admin
from django.urls import path,include
from app01 import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('app01.urls')),
    # path('home/', views.home),

]
