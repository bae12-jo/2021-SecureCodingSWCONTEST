from django.db import models
import hashlib
# 유저모델 import?

# 결제 요청
class Pay(models.Model):
    user_id = models.ForeignKey(max_length=20)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pay_check = models.BooleanField(default=False)
    # form = MyForm(initial={'pay_check':True))

    def __str__(self):
        return f'{self.price}'

# 트랜젝션 생성
class PayTransactionManager(models.Manager):
    def create_transaction(self, user_id, amount, success=None, transaction_status=None):
        if not user_id:
            raise ValueError("주문시 문제가 발생했습니다.")




class PayTransaction(models.Model):
    user_id = models.CharField(max_length=20) # fk로 유저 정보 가져오는 것으로 수정
    pay_id = models.CharField(max_length=220, unique=True, blank=True)
    transaction_id = models.CharField(max_length=220, null=True, blank=True)
    amount = models.FloatField(default=0)
    transaction_status = models.CharField(max_length=220, null=True, blank=True)
    type = models.CharField(max_length=120, blank=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return f'{str.pay_id}'

    class Meta:
        ordering = ['-created']
