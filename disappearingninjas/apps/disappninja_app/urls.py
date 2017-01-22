from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$',views.ninja),
     url(r'^ninjas/(?P<id>\w+)$', views.show)
]
