# video/urls.py
# from django.conf.urls import url, include
from django.urls import path, include
from . import views

urlpatterns = [path(r"^$", views.video_list, name="list")]

