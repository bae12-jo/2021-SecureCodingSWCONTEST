from django.db import models
from common.models import User
# Create your models here.
class Group(models.Model):
    group_name=models.CharField(max_length=100)
    deposit=models.FloatField()
    fine=models.FloatField()
    REWARD_CHOICES=[
        ' 1/N, N=number of members',
        ' All to the single winner',
    ]
    reward=models.CharField(choices=REWARD_CHOICES)
    teammate=models.ForeignKey(User,on_delete=models.CASCADE)
    rule=models.CharField(max_length=500)
