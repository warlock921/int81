#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-17 22:43:21
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : https://github.com/warlock921
# @Version : $Id$

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from .models import ReadNum,ReadDetail

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
    
