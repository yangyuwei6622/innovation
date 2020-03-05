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
class TypeInfo(models.Model):
    tTitle = models.CharField(max_length=30 )
    isDelete = models.BooleanField(default=False)
class shopInfo(models.Model):
    sTitle = models.CharField(max_length=50)
    sPic = models.ImageField(upload_to='shops')
    sPrice= models.DecimalField(max_digits= 5 ,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    sUnit = models.CharField(max_length=50)
    sStar = models.IntegerField()
    sContent = models.CharField(max_length=600)
    sBrief = models.CharField(max_length=200)
    sType = models.ForeignKey(TypeInfo)
    #sAdv = models.BooleanField(default=False)




