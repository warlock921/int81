#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-23 11:14:58
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : https://github.com/warlock921
# @Version : $Id$

from django.urls import path
from . import views

urlpatterns = [
    path('update-comment/', views.update_comment, name='update_comment'),
]
