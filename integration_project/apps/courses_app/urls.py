from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^courses$', views.index,name = 'courses_index' ),
    url(r'^addcourse$',views.add, name = 'addcourse'),
    url(r'^remove/(?P<id>\d+)$',views.remove, name = 'remove'),
    url(r'^confirmdelete/(?P<id>\d+)$',views.delete, name = 'delete'),
]
