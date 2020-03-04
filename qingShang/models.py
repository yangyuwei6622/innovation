from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uName = models.CharField(max_length=20)
    uPwd = models.CharField(max_length= 60)
    uEmail = models.CharField(max_length=60)
    uEmployer = models.CharField(max_length=20 ,default='')
    uAddress = models.CharField(max_length=60,default='')
    uPhoneNum = models.CharField(max_length=11,default='')

    #不写default 默认必须有值
