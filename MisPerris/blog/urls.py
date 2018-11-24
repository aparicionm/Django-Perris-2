from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.res_list, name="list"),
    url(r'^res/(?P<pk>[0-9]+)/$', views.res_detail, name='res_detail'),
    url(r'^res/new/$', views.res_new, name='res_new'),
    url(r'^res/(?P<pk>[0-9]+)/edit/$', views.res_edit, name='res_edit'),
    url(r'^res/(?P<pk>[0-9]+)/delete/$', views.res_delete, name='res_delete'),
]
