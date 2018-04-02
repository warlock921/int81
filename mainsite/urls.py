#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-02 16:05:20
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : http://www.thinkheh.cn
# @Version : $Id$

from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index')
]
