#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "stay_sun"

from django.forms import Form
from django.forms import fields
from django.forms import widgets
from cmdb import models


class MenuForm(Form):
    caption = fields.CharField(
        required=True,
        error_messages={'required': '目录名不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    url  = fields.CharField(
        required=False,
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    parent_id = fields.ChoiceField(
        required=False,
        choices=[],
        widget=widgets.Select(attrs={'class': 'form-control'},)
    )

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['parent_id'].choices = models.Menu.objects.values_list('id', 'caption')




class HostForm(Form):
    hostname = fields.CharField(
        required=True,
        error_messages={'required': '主机名不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    host_ip = fields.GenericIPAddressField(
        required=True,

        error_messages={'required': 'ip不能为空', 'invalid': 'ip格式错误'},
        widget = widgets.TextInput(attrs={'class': 'form-control'}))

    ssh_port = fields.CharField(
        required=True,
        error_messages={'required': '端口不能为空', 'invalid': '端口格式错误'},
        widget=widgets.TextInput(attrs={'class': 'form-control'}))
    project_name = fields.CharField(
        required=False,
        error_messages={'required': '项目不能为空', 'invalid': '项目错误'},
        widget=widgets.TextInput(attrs={'class': 'form-control'}))
    sl_id = fields.ChoiceField(
        choices=[],
        widget=widgets.Select(attrs={'class': 'form-control'},)
    )

    def __init__(self, *args, **kwargs):
        super(HostForm, self).__init__(*args, **kwargs)
        self.fields['sl_id'].choices = models.Service_Line.objects.values_list('id', 'service_line_name')



class RegisterForm(Form):
    username = fields.CharField(required=True,min_length=6,max_length=18,error_messages={'required': '用户名不能为空'},)
    email = fields.EmailField(required=True,min_length=6,max_length=18, error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})
    password = fields.CharField(min_length=12, error_messages={'required': '密码不能为空', 'invalid': '密码格式错误'})




class UserForm(Form):
    username = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空', 'invalid': '密码格式错误'})

    email=fields.EmailField(
        required=True,
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})

    phone=fields.IntegerField(
        required=True,
        error_messages={'required': '电话不能为空'}

    )

    sl_id = fields.MultipleChoiceField(
        choices=[],
        widget=widgets.SelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['sl_id'].choices = models.Service_Line.objects.values_list('id', 'service_line_name')