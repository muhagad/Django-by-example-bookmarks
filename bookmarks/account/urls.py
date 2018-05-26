from django.conf.urls import url, include
from . import views


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$', include('django.contrib.auth.views.login'), name='login'),
    url(r'^logout/$', include('django.contrib.auth.views.logout'), name='logout'),
    url(r'^logout-then-login/$', include('django.contrib.auth.views.logout_then_login'), name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
]