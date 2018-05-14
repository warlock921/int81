#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 23:04:14
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : https://github.com/warlock921
# @Version : $Id$

from django import forms

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput())
    object_id = forms.IntegerField(widget=forms.HiddenInput())
    comment_content = forms.CharField(label="评论内容", widget=forms.Textarea(attrs={'rows':4, 'class':"form-control"}))
