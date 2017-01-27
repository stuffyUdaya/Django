from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$',views.index,name = 'lreg_index'  ),
    url(r'^process$', views.process, name = 'processreg'),
    url(r'^login$', views.login, name= 'processlog'),
    url(r'^success$', views.success, name = 'success'),
    url(r'^logout$', views.logout, name = 'logout'),
    ]
