"""
URL configuration for Jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authuser import views
admin.site.site_header= "Jobmela Admin"
admin.site.site_title= "Jobmela Admin Portal"
admin.site.index_title= "welcome to Jobmela Portal"
app_name='authuser'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('cregister/', views.cregister, name='cregister'),
    path('hrregister/', views.hrregister, name='hrregister'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('navbar', views.navbar, name='navbar'),
    path('Companies', views.Companies, name='Companies'),
    
]
