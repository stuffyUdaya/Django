from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^addbook/(?P<id>\d+)$', views.addbook),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^addreview/(?P<uid>\d+)/(?P<bid>\d+)$', views.addreview),
    url(r'^viewbook/(?P<id>\d+)$', views.viewbook),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home),


]
