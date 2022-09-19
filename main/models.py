from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=30, verbose_name="项目名称")
    desc = models.CharField(max_length=500, blank=True, null=True, verbose_name="项目描述")
    created_by = models.ForeignKey(User, null=True, verbose_name="创建人", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name
