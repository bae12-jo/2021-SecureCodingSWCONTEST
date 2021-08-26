import requests
from django.conf import settings

# 아임포트 고유번호 : imp_uid, 가맹점지정 고유번호 : merchant_uid, 취소 사유 : reason, 취소 요청 금액 : amount,
# 카드 소유자 정보 : customer_info

# api key, secret key 통해 iamport에서 로그인
def get_token() :
    # iamport 자체 요청 사항
    access_data = {
        'imp_key': 'settings.IAMPORT_KEY',
        'imp_secret': 'settings.IAMPORT_SECRET'
    }
    url = "https://api.iamport.kr/users/getToken"

    # 서버에 접속해 데이터 받아오기
    request = requests.post(url, data = access_data)
    # request로 받아온 data json 형식으로 해석
    access_res = request.json()

    if access_res['code'] is 0:
        return access_res['response']['access_token']
    else:
        return None

# 특정 pay_id와 금액을 정해 결제 요청 (유저 요청 금액 / 결제 금액 일치 확인)
def payments_prepare(pay_id, amount, *args, **kwargs):
    access_token = get_token()

    if access_token:
        access_data = {
            'merchant_uid': pay_id,
            'amount': amount
        }
        url = "https://api.iamport.kr/payments/prepare"
        headers = {
            'Authorization': access_token
        }
        request = requests.post(url, data=access_data, headers=headers)
        res = request.json()

        if res['code'] != 0:
            raise ValueError("API 연결 오류")

    else:
        raise ValueError("토큰을 받지 못했습니다.")

# 결제 완료 후,실제로 결제가 맞게 됐는지 확인
def check_transaction(pay_id, *args, **kwargs) :
    access_token = get_token()

    if access_token:
        url = "https://api.iamport.kr/payments/find/" + pay_id
        headers = {
            'Authorization': access_token
        }
        request = requests.post(url, headers=headers)
        res = request.json()

        if res['code'] == 0:
            context = {
                'imp_id': res['response']['imp_uid'],
                'merchant_order_id':res['response']['merchant_uid']
                'amount':res['response']['amount'],
                'status':res['response']['status'],
                'type':res['response']['pay_method'],
                'receipt_url':res['response']['receipt_url']
            }
            return context
        else:
            return None
    else:
        raise ValueError("토큰을 받지 못했습니다.")

