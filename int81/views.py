#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-11 16:45:51
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : http://www.thinkheh.cn
# @Version : $Id$

from django.shortcuts import render_to_response

def index(request):
    context = {}
    return render_to_response('index.html', context)

