from django.db import models

# 금액대 선택 기준
class PriceChoice(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return self.name

# 주문자의 정보 기록
class OrderReq(models.Model):
    username = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    pay_check = models.BooleanField(default=False)
    # form = MyForm(initial={'pay_check':True))

    def __str__(self):
        return str(self.id)
    
    def get_total_price(self):
        total_price = self.price

# 어떤 가격을 선택했는지 저장
class OrderPrice(models.Model):
    order = models.ForeignKey(OrderReq, on_delete=models.CASCADE, related_name='items')
    choice = models.ForeignKey(PriceChoice, on_delete=models.PROTECT, related_name='order_price')
    price = models.FloatField()

    def __str__(self):
        return str(self.id)

# orderTransaction db action
import random
from .iamport import payments_prepare, check_transaction
class OrderTransactionManager(models.Manager):
    def create_new(self, order, amount, success=None, transaction_status=None):
        if not order:
            raise ValueError("주문 정보에 오류가 발생했습니다.")

        # 주문 번호 생성
        random_num = random.randrange(10000, 10000000)
        order_num = str(order.created + random_num)
        merchant_order_id =  str(order_num)

        payments_prepare(merchant_order_id, amount)

        transaction = self.model(
            order=order,
            merchant_order_id=merchant_order_id,
            amount=amount
        )

        if success is not None:
            transaction.success = success
            transaction.transaction_status = transaction_status

            transaction.save()  # transaction을 db에 저장

        def get_transaction(self, merchant_order_id):
            result = check_transaction(merchant_order_id)
            if result['status'] == 'paid':
                return result
            else:
                return None

# 주문정보 저장
class OrderTransaction(models.Model):
    order = models.ForeignKey(OrderReq, on_delete=models.CASCADE)
    merchant_order_id = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_status = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = OrderTransactionManager()

    def __str__(self):
        return str(self.order.id)

# 결제 유효성 체크
def payment_validation(sender, instance, created, *args, **kwargs):
    if instance.transaction_id:
        iamport_transaction = OrderTransaction.objects.get_transaction(merchant_order_id=instance.merchant_order_id)
        merchant_order_id = iamport_transaction['merchant_order_id']
        imp_id = iamport_transaction['imp_id']
        amount = iamport_transaction['amount']

        local_transaction = OrderTransaction.objects.filter(merchant_order_id=merchant_order_id, transaction_id=imp_id, amount=amount).exists()

        if not iamport_transaction or not local_transaction:
            raise ValueError("잘못된 거래입니다.")

    from django.db.models.signals import post_save
    post_save.connect(payment_validation, sender=OrderTransaction)
