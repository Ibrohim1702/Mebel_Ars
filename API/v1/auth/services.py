import base64
import datetime

from django.contrib.sites import requests
from pytz import timezone
from rest_framework.authtoken.models import Token
import requests
import json
from account.models import User, ServerToken


def regis(self, params):
    user = User.objects.filter(username=params.get("username")).first()
    if user:
        return {
            "Error": "Bunaqa foydalanuvchi bor"
        }

    serilizer = self.get_serializer(data=params)
    serilizer.is_valid(raise_exception=True)
    root = serilizer.create(serilizer.data)
    root.set_password(params['password'])
    root.save()
    token = Token()
    token.user = root
    token.save()

    return {
        "token": token.key
    }


def loqinapi(self, params):

    nott = "username" if 'username' not in params else "password" if "password" not in params else None
    if nott:
        return {
            "Error": f"f{nott} toliq toldirilmagan"
        }

    user = User.objects.filter(username=params['username']).first()
    if not user:
        return {
            "Error": "User topilmadi"
        }
    if not user.check_password(params['password']):
        return {
            "Error": "Parol xato "
        }

    token = Token.objects.get_or_create(user=user)
    return {
        "token": token[0].key
    }





def code_decode(code, decode=False):
    if decode:
        print("shifrdan ochaman")
    else:
        return base64.b16encode(str(code).encode("utf-8"))

a = code_decode("Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjI0NjYsInJvbGUiOiIiLCJkYXRhIjp7ImlkIjoyNDY2LCJuYW1lIjoiSWJyb2hpbSBRb2JpbG92IiwiZW1haWwiOiJpYnJhaGlta2FiaWxvdkBnbWFpbC5jb20iLCJyb2xlIjoiIiwiYXBpX3Rva2VuIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SnpkV0lpT2pJME5qWXNJbkp2YkdVaU9pSWlMQ0prWVhSaElqcDdJbWxrSWpveU5EWTJMQ0p1WVcxbElqb2lTV0p5YjJocGJTQlJiMkpwYkc5Mklpd2laVzFoYVd3aU9pSnBZbkpoYUdsdGEyRmlhV3h2ZGtCbmJXRnBiQzVqYjIwaUxDSnliMnhsSWpvaUlpd2lZWEJwWDNSdmEyVnVJam9pWlhsS01HVllRV2xQYVVwTFZqRlJhVXhEU21oaVIyTnBUMmxLU1ZWNlNURk9hVW81TG1WNVNuIiwic3RhdHVzIjoiYWN0aXZlIiwic21zX2FwaV9sb2dpbiI6ImVza2l6MiIsInNtc19hcGlfcGFzc3dvcmQiOiJlJCRrIXoiLCJ1el9wcmljZSI6NTAsInVjZWxsX3ByaWNlIjoxMTUsInRlc3RfdWNlbGxfcHJpY2UiOjAsImJhbGFuY2UiOjUwMDAsImlzX3ZpcCI6MCwiaG9zdCI6InNlcnZlcjEiLCJjcmVhdGVkX2F0IjoiMjAyMy0wMi0wOFQxMjoyNjozOC4wMDAwMDBaIiwidXBkYXRlZF9hdCI6IjIwMjMtM"
            "DItMTVUMTI6Mzk6MTIuMDAwMDAwWiJ9LCJpYXQiOjE2NzY0NjU4MjYsImV4cCI6MTY3OTA1NzgyNn0.CKm40dFIXtuOXEKJeDnMfwy-ZyWzGONLBR7mGNQLXHA", decode=True)

print(a)




def send_sms(phone, otp):
    msg = f"Maxfiy kod: {otp} buni hech qachon adminlar so`ramaydi"


    url = "http://notify.eskiz.uz/api/message/sms/send"


    token = ServerToken.objects.get(key="sms")

    payload = json.dumps({
        "mobile_phone": f"{phone}",
        "message": msg,
        "from": "4546",
        "callback_url": "http://0000.uz/test.php"
    })
    headers = {
        'Authorization': f'Bearer {token.token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.json()



def check_otp_expire(otp):
    now = datetime.datetime.now()
    otp_date = otp.create_at

    if (now-otp_date).total_seconds() > 120:
        otp.expire = True
        otp.save()
        return False
    else:
        return True
