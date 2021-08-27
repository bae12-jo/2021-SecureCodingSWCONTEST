from django.db.models import ManyToManyField
from django.db import models
from django.urls import reverse
from django import forms
from common.models import User
# Create your models here.
class Group(models.Model):
    #이름
    group_name=models.CharField(max_length=100,primary_key=True)
    #돈 관련 사항
    deposit=models.FloatField(null=True)
    fine=models.FloatField(null=True)
    REWARD_CHOICES=[
        (1,' 1/N, N=number of members'),
        (2,' All to the single winner'),
    ]
    reward=models.CharField(choices=REWARD_CHOICES, max_length=100,null=True)
    money_sum=models.FloatField(null=True)#벌금 모음
    #사람
    '''
    potential_teammate=ManyToManyField(
        'common.User',
        related_name='teammates',
        related_query_name='teammate',

    )
    '''
    #potential_teammate=User.objects.all()

    leader=models.CharField(max_length=100,default="Song")
    teammate=models.CharField(max_length=100,null=True)
    #규칙
    rule=models.CharField(max_length=500,null=True)

    #leader가 group을 수정하는 동안은 결제 버튼을 누를 수 없다.
    pemitted_to_pay=models.BooleanField(default=True)

    class Meta:
        ordering=['group_name']
        verbose_name='group'
        verbose_name_plural='groups'
    def __str__(self):
        return self.group_name
    def get_absolute_url(self):
        return reverse('my_groups_detail',args=[str(self.group_name)])
    def create(cls,group_name,deposit,fine,reward,leader,rule):
        newgroup=cls(
            group_name=group_name,
            deposit=deposit,
            fine=fine,
            reward=reward,
            leader=leader,
            rule=rule
        )
        return newgroup
'''
#debug를 위한 group instance testing
new_group=Group.create(
    group_name='wake-up study',
    deposit=10000,
    fine=100,
    reward=1,
    leader="Joe",
    rule="none",

)
'''
