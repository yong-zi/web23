# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    cityname = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # 逆向生成模型类时自动带的，managed = False 意思是等再次生成并执行迁移文件时不执行该模型类
        db_table = 'city'


class SysPosition(models.Model):
    area_name = models.CharField(max_length=255, blank=True, null=True)
    area_code = models.IntegerField(blank=True, null=True)
    city_code = models.CharField(max_length=11, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    area_index = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False # 逆向生成模型类时自动带的，managed = False 意思是等再次生成并执行迁移文件时不执行该模型类
        db_table = 'sys_position'
