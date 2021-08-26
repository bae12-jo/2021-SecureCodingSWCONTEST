from django.db import models
from django.urls import reverse

from common.models import User
# Create your models here.
class Group(models.Model):
    #이름
    group_name=models.CharField(max_length=100)
    #돈 관련 사항
    deposit=models.FloatField()
    fine=models.FloatField()
    REWARD_CHOICES=[
        (1,' 1/N, N=number of members'),
        (2,' All to the single winner'),
    ]
    reward=models.CharField(choices=REWARD_CHOICES, max_length=100)
    #사람
    teammate=models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='teammates',
        related_query_name='teammate'

    )
    leader=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    #규칙
    rule=models.CharField(max_length=500)
    can_pay=models.BooleanField(default=True)
    class Meta:
        ordering=['group_name']
        verbose_name='group'
        verbose_name_plural='groups'
    def __str__(self):
        return self.group_name
    def get_absolute_url(self):
        return reverse('my_groups_detail',args=[str(self.group_name)])


class Record(models.Model):
    associated_group=models.OneToOneField(
        Group,
        on_delete=models.CASCADE
    )
    '''
    associated_user=models.OneToOneField{
        User,
        on_delete=models.CASCADE
    }
    '''
    total_fine=models.FloatField()
    fine_count=models.IntegerField()

