'''
Author: LetMeFly
Date: 2022-02-02 12:32:03
LastEditors: LetMeFly
LastEditTime: 2022-02-04 11:05:36
'''
from django.db import models

# Create your models here.

class user(models.Model):
    userid = models.CharField(verbose_name="openid", max_length=40, unique=True)
    session_key = models.CharField(verbose_name="session_key", max_length=40)
    remark = models.CharField(verbose_name="备注", max_length=50, null=True)


class diaries(models.Model):
    userid = models.CharField(verbose_name="openid", max_length=40)
    content = models.CharField(verbose_name="日记内容", max_length=1024)
