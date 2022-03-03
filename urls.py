from django.conf.urls import url
from django.contrib import admin
import views


app_name = 'demo1'

urlpatterns = [
    url(r'^admin/login', views.login),
    url(r'^admin/upload', views.upload),
    url(r'^admin/display', views.display),
]