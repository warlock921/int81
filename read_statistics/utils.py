#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-17 22:43:21
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : https://github.com/warlock921
# @Version : $Id$

import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum,ReadDetail
from mainsite.models import Blog

def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)
    if not request.COOKIES.get(key):
        #总阅读数加1
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()
        #当天阅读数加1
        detail_date = timezone.now().date()
        readdetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, detail_date=detail_date)
        readdetail.read_num += 1
        readdetail.save()
    return key

def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, detail_date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums

def get_today_hot_data():
    today = timezone.now().date()
    blogs = Blog.objects.filter(read_details__detail_date=today) \
                      .values('id', 'title') \
                      .annotate(read_num_sum=Sum('read_details__read_num')) \
                      .order_by('-read_num_sum')
    # read_details = ReadDetail.objects.filter(content_type=content_type, detail_date=today).order_by('-read_num')
    return blogs

def get_yesterday_hot_data():
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    blogs = Blog.objects.filter(read_details__detail_date=yesterday) \
                      .values('id', 'title') \
                      .annotate(read_num_sum=Sum('read_details__read_num')) \
                      .order_by('-read_num_sum')
    # read_details = ReadDetail.objects.filter(content_type=content_type, detail_date=yesterday).order_by('-read_num')
    return blogs

def get_week_hot_data():
    today = timezone.now().date()
    day_nums = today.isoweekday()
    monday = today - datetime.timedelta(days=day_nums)
    blogs = Blog.objects.filter(read_details__detail_date__range=(monday,today)) \
                      .values('id', 'title') \
                      .annotate(read_num_sum=Sum('read_details__read_num')) \
                      .order_by('-read_num_sum')
    return blogs
    
