from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from group.models import Record
from common import forms


class User(AbstractUser):
    #pre-set

    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=100,default="")

    #optional
    email=models.EmailField(_('email address',widget=forms.EmailInput({'placeholder': 'test@example.com'})),unique=True)

    USERNAME_FIELD='username'
    PASSWORD_FIELD='password'
    REQUIRED_FIELDS=['email']

    #개인 정보
    phone = models.CharField(max_length=20,default=None)
    address = models.CharField(max_length=50,default=None)

    #돈
    balance = models.CharField(max_length=50,default=None)
    record = models.OnetoManyField(Record, on_delete=models.CASCADE)
    
    #그룹
    groups=models.ForeignKey(Group,on_delete=models.PROTECT)
    def str(self):
        return self.email
'''
class User(models.Model):
    pass

#create test user --debug
user=User.objects.create_user('green','admin@greenbalm.com','balm')
user.first_name='yeonkoung'
user.last_name='kim'
user.save()
'''
