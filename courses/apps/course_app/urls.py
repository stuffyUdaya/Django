from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^addcourse$',views.add),
    url(r'^remove/(?P<id>\d+)$',views.remove),
    url(r'^confirmdelete/(?P<id>\d+)$',views.delete),
]
