# -*- coding: utf-8 -*-

from django.conf.urls import *

import views

urlpatterns = patterns('',
    (r'^$', views.hello1),
    (r'hello2', views.hello2),
    (r'hello3', views.hello3),
)