#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-24 00:00:21
# @Author  : warlock921 (caoyu921@163.com)
# @Link    : https://github.com/warlock921
# @Version : $Id$

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"请输入用户名"}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"请输入密码"}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data

class RegForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=3, label="用户名", widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"请输入用户名"}))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'class':"form-control", 'placeholder':"请输入邮箱"}))
    password = forms.CharField(min_length=8, label="密码", widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"请输入密码"}))
    password_again = forms.CharField(min_length=8, label="再次输入密码", widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"请再输入一次密码"}))
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("用户名已经存在")
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("邮箱已经存在")
        else:
            return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError("两次输入的密码不一致")
        else:
            return password_again