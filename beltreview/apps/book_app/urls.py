from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^addbook/(?P<id>\d+)$', views.addbook),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^viewbook/(?P<id>\d+)$', views.viewbook),


]
