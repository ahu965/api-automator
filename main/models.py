from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30, verbose_name="项目名称")
    desc = models.CharField(max_length=500, blank=True, null=True, verbose_name="项目描述")
    created_by = models.ForeignKey(User, null=True, verbose_name="创建人", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name


# 分类表」、「接口表」、「用例表
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="分类名称")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父分类", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, verbose_name="创建人", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Api(models.Model):
    METHOD_TYPE = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE')
    )
    BODY_TYPE = (
        ('NONE', '默认没有请求体'),
        ('JSON', 'JSON格式'),
        ('FORM', '表单格式'),
        ('BINARY', '二进制格式，例如文件'),
    )
    name = models.CharField(max_length=50, verbose_name="接口名称")
    desc = models.CharField(max_length=500, blank=True, null=True, verbose_name="接口描述")
    method = models.CharField(max_length=10, choices=METHOD_TYPE, verbose_name="请求方式")
    path = models.CharField(max_length=500, blank=True, null=True, verbose_name="接口路径")
    params = models.CharField(max_length=500, blank=True, null=True, verbose_name="请求参数，以json串进行保存")
    headers = models.CharField(max_length=500, blank=True, null=True, verbose_name="请求头，以json串进行保存")
    body = models.TextField(blank=True, null=True, verbose_name="请求体，以json串进行保存")
    body_type = models.CharField(max_length=20, choices=BODY_TYPE, default="NONE", verbose_name="请求体类型")
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name="分类", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, verbose_name="创建人", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "接口"
        verbose_name_plural = verbose_name


class Case(models.Model):
    name = models.CharField(max_length=50, verbose_name="用例名称")
    desc = models.CharField(max_length=500, blank=True, null=True, verbose_name="项目描述")
    method = models.CharField(max_length=10, choices=Api.METHOD_TYPE, verbose_name="请求方式")
    path = models.CharField(max_length=500, blank=True, null=True, verbose_name="接口路径")
    params = models.CharField(max_length=500, blank=True, null=True, verbose_name="请求参数，以json串进行保存")
    headers = models.CharField(max_length=500, blank=True, null=True, verbose_name="请求头，以json串进行保存")
    body = models.TextField(blank=True, null=True, verbose_name="请求头，以json串进行保存")
    api = models.ForeignKey(Api, verbose_name="所属接口", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, null=True, verbose_name="创建人", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "用例"
        verbose_name_plural = verbose_name


class Env(models.Model):
    PROTOCOL_TYPE = (
        ('HTTP', 'HTTP'),
        ('HTTPS', 'HTTPS')
    )

    name = models.CharField(max_length=50, verbose_name="环境名称")
    desc = models.CharField(max_length=500, blank=True, null=True, verbose_name="环境描述")
    protocol = models.CharField(max_length=10, choices=PROTOCOL_TYPE, verbose_name="协议")
    domain = models.CharField(max_length=100, verbose_name="环境IP/域名")
    port = models.CharField(max_length=10, verbose_name="端口")
    created_by = models.ForeignKey(User, null=True, verbose_name="创建人", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "环境管理"
        verbose_name_plural = verbose_name
