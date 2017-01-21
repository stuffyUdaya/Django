from django.conf.urls import url,include
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^new_word$', views.newword ),
    url(r'^$', views.index ),
    url(r'^clear_counter$',views.clear ),
]
