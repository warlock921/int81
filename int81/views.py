#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-11 16:45:51
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : http://www.thinkheh.cn
# @Version : $Id$

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.urls import reverse
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data, get_week_hot_data
from mainsite.models import Blog

def index(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    today_hot_data = cache.get('today_hot_data')
    if today_hot_data is None:
        today_hot_data = get_today_hot_data()[:5]
        cache.set('today_hot_data', today_hot_data, 3600)
        print("系统创建了缓存 today_hot_data %s" % type(today_hot_data) )
    else:
         print("读取系统缓存数据 today_hot_data %s" % type(today_hot_data))

    yesterday_hot_data = cache.get('yesterday_hot_data')
    if yesterday_hot_data is None:
        yesterday_hot_data = get_yesterday_hot_data()[:5]
        cache.set('yesterday_hot_data', yesterday_hot_data, 3600)
        print("系统创建了缓存 yesterday_hot_data %s" % type(yesterday_hot_data) )
    else:
        print("读取系统缓存数据 yesterday_hot_data %s" % type(yesterday_hot_data))

    week_hot_data = cache.get('week_hot_data')
    if week_hot_data is None:
        week_hot_data = get_week_hot_data()[:5]
        cache.set('week_hot_data', week_hot_data, 3600)
        print("系统创建了缓存 week_hot_data %s" % type(week_hot_data) )
    else:
        print("读取系统缓存数据 week_hot_data %s" % type(week_hot_data))

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = today_hot_data
    context['yesterday_hot_data'] = yesterday_hot_data
    context['week_hot_data'] = week_hot_data

    #不使用缓存的情况
    # context['today_hot_data'] = get_today_hot_data()[:5]
    # context['yesterday_hot_data'] = get_yesterday_hot_data()[:5]
    # context['week_hot_data'] = get_week_hot_data()[:5]
    return render(request, 'index.html', context)

def user_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if user is not None:
        login(request, user)
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message':"出错啦！！！"})
