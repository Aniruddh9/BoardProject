"""WebBoard URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path
from boards import views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/',account_views.signup, name='signup'),
    re_path('^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    re_path('^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),

]
