# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Jiacaiwang(models.Model):
    index = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=250, blank=True, null=True)
    experience = models.CharField(max_length=250, blank=True, null=True)
    information = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jiacaiwang'


class TBrand(models.Model):
    tmname = models.CharField(max_length=255, blank=True, null=True)
    reg_name = models.CharField(max_length=255, blank=True, null=True)
    regnum = models.CharField(max_length=255, blank=True, null=True)
    app_date = models.CharField(max_length=255, blank=True, null=True)
    regname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_brand'


class TBrandLog(models.Model):
    charindex = models.CharField(max_length=255, blank=True, null=True)
    pn = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_brand_log'


class TEmployee(models.Model):
    job = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_employee'


class TJob51Async(models.Model):
    job = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_job51_async'


class TJuxianwang(models.Model):
    number_1common_info_current_situation_job_intentioncommon_info = models.CharField(db_column='1common_info\r\ncurrent_situation\r\njob_intentioncommon_info', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    current_situation = models.TextField(blank=True, null=True)
    job_intention = models.TextField(blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    project_experience = models.TextField(blank=True, null=True)
    edu_experience = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_juxianwang'


class TLogJx(models.Model):
    jobindex = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_log_jx'
