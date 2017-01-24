from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addfriend$', views.addfriend ),
    url(r'^pairfriends$',views.pairfriend),
]
