from django.db import models

#定义设置模型类DeviceInfo
class DeviceInfo(models.Model):
    id = models.IntegerField(max_length=10,primary_key=True,verbose_name='设备ID')
    type = models.CharField(max_length=10,verbose_name='设备类型')
    model = models.CharField(max_length=10,verbose_name='设备型号')
    situation = models.CharField(max_length=64, verbose_name='设备状态')
    area = models.CharField(max_length=64, verbose_name='设备位置')
    #updatetime = models.DateField(verbose_name='修改时间')
