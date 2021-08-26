from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    #pre-set

    username = models.CharField(max_length=100,unique=True,default="",primary_key=True)
    password = models.CharField(max_length=100,default="")

    #optional
    email=models.EmailField(_('email address'),null=True,unique=True)

    USERNAME_FIELD='username'
    PASSWORD_FIELD='password'
    REQUIRED_FIELDS=['email']

    #개인 정보
    address = models.CharField(max_length=50,default=None,null=True)

    #돈
    balance = models.FloatField(max_length=50,default=0,null=True)

    #그룹
    #그냥 디폴트 있음
    #후보키는 결국 하나만 되는 거야groups=models.ForeignKey('group.Group',on_delete=models.PROTECT,blank=True)
    #벌금 관리
    paid_fine={}
    '''
    벌금 count를 할 때 group이름이 key로 없으면 -->paid_fine[그룹이름]=1*그룹의 벌금
    있으면-->paid_fine[그룹이름]+=1*그룹의 벌금
     '''

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
