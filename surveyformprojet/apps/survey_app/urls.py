from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$', views.index ),
    url(r'^results$', views.showuser),
    url(r'^goback$', views.back),
]
