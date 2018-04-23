#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-24 00:00:21
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : https://github.com/warlock921
# @Version : $Id$

from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", widget = forms.TextInput(attrs={'class':"form-control", 'placeholder':"请输入用户名"}))
    password = forms.CharField(label="密码", widget = forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"请输入密码"}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data