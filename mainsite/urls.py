#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-02 16:05:20
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : http://www.thinkheh.cn
# @Version : $Id$

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('blog-type-selected/<int:blog_type_pk>', views.blog_type_selected, name='blog_type_selected'),
    path('blog-date-selected/<int:year>/<int:month>', views.blog_date_selected, name='blog_date_selected'),
]
