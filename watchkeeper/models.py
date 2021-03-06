# _*_ coding:utf-8 _*_
from django.db import models


# Create your models here.

class watchkeeper(models.Model):
    tag_default = 0
    tag_need_not = 1
    tag_choice = (
        (tag_default, '需要'),
        (tag_need_not, '不需要')
    )
    name = models.CharField(default="", blank=True, verbose_name='姓名', max_length=30)
    phone = models.CharField(verbose_name='电话', blank=True, max_length=11, default="")
    qq = models.CharField(verbose_name='QQ号', blank=True, max_length=13, default="")
    email = models.EmailField(verbose_name='邮箱', blank=True, default="")
    tag = models.IntegerField(default=tag_default, choices=tag_choice, verbose_name='是否需要值班')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '人员管理'
        verbose_name_plural = '人员管理'


class ServiceInfo(models.Model):
    name = models.CharField(default="", blank=True, verbose_name='服务名称', max_length=30)
    packgeName = models.CharField(default="", blank=True, verbose_name='包名称', max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '服务管理'
        verbose_name_plural = '服务管理'


class RunEnv(models.Model):
    env_name = models.CharField(default="stage", blank=True, verbose_name='运行环境', max_length=30)

    def __unicode__(self):
        return self.env_name

    class Meta:
        verbose_name = '环境管理'
        verbose_name_plural = '环境管理'


class watchlist(models.Model):
    name = models.CharField(max_length=30)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        verbose_name = '值班表'
        verbose_name_plural = '值班表'

    def __unicode__(self):
        return self.name


class serverInfo(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP地址')
    innerip = models.GenericIPAddressField(default='127.0.0.1', null=True, blank=True, verbose_name='内网IP')
    nickname = models.CharField(verbose_name='别名', max_length=20)
    # service = models.TextField(verbose_name='运行服务')
    service = models.ManyToManyField(ServiceInfo, blank=True, verbose_name=u'运行服务')
    cpu = models.IntegerField(verbose_name='CPU(核)')
    mem = models.IntegerField(verbose_name='内存（G）')
    system = models.TextField(verbose_name='操作系统')
    role = models.ForeignKey(RunEnv, default="", blank=True, verbose_name=u'运行环境', max_length=20)

    class Meta:
        verbose_name = '主机管理'
        verbose_name_plural = '主机管理'

    def get_service(self):
        return ",".join([p.name for p in self.service.all()])

    get_service.short_description = '运行服务'

    def __unicode__(self):
        return self.ip
