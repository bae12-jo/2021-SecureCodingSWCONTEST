from django.db.models import ManyToManyField
from django.db import models
from django.urls import reverse
from django import forms
from common.models import User
# Create your models here.
class Group(models.Model):
    #그룹 이름
    group_name=models.CharField(max_length=100,primary_key=True)
    #돈 관련 사항
    deposit=models.FloatField(null=True) #보증금 고정가격
    fine=models.FloatField(null=True) #벌금 고정가격
    REWARD_CHOICES=[
        (1,' 1/N, N=number of members'),
        (2,' All to the single winner'),
    ]#모인 벌금 분배 방식
    reward=models.CharField(choices=REWARD_CHOICES, max_length=100,null=True)
    money_sum=models.FloatField(null=True)#실제로 수거된 벌금 모음
    #사람
    '''
    potential_teammate=ManyToManyField(
        'common.User',
        related_name='teammates',
        related_query_name='teammate',

    )
    '''
    #potential_teammate=User.objects.all() 
    #option을 User.objects.all()으로 할 수 없다.
    #그렇다고 ManyToManyField().all()도 안된다.
    #게다가 여러명을 form에서 고르게 해주는 것은 django.forms의 MultipleChoiceField인데 모델과 상호호환이 안 되고 있다.

    leader=models.CharField(max_length=100,default="Song")#**later** manager model 이용해서 만들어보기
    teammate=models.CharField(max_length=100,null=True)
    
    #규칙
    rule=models.CharField(max_length=500,null=True)

    #leader가 group 내용을 수정하는 동안은 teammate의 개인들은 벌금 결제 버튼을 누를 수 없다. (mutex만들어야 함)
    pemitted_to_pay=models.BooleanField(default=True)

    class Meta:
        ordering=['group_name']
        verbose_name='group'
        verbose_name_plural='groups'
    def __str__(self):
        return self.group_name
    #group인스턴스마다 detail page를 할당받을 수 있도록 다이나믹 url을 만들기 위한 부분
    def get_absolute_url(self):
        return reverse('my_groups_detail',args=[str(self.group_name)])
    #테스트를 위해 인스턴스를 만드는 함수
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
