from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uName = models.CharField(max_length=20)
    uPwd = models.CharField(max_length= 60)
    uEmail = models.CharField(max_length=60)
    uEmployer = models.CharField(max_length=20)
    uAddress = models.CharField(max_length=60)
    uPhoneNum = models.CharField(max_length=11)
