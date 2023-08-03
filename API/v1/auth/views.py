import binascii
import os
import random
from collections import OrderedDict

from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from account.models import User, OTP
from dashboard.models import Product, Likes
from .serializer import UserSerializer
from .services import regis, loqinapi, code_decode, send_sms, check_otp_expire


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


class AuthView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, requests, *args, **kwargs):
        data = requests.data
        method = data.get("method")
        params = data.get("params")
        if not method:
            return Response({
                "Error": "method kiritlishi kerak"
            })
        if params is None:
            return Response({
                "Error": "params kiritlishi kerak"
            })

        if method == "regis":
            return Response(regis(self, params))
        elif method == "login":
            return Response(loqinapi(self, params))
        elif method == "step_one":
            nott = "phone" if "phone" not in params else None


            if nott:
                return Response({
                    "Error": "phon.params bo`lishi kerak"
                })

            if len(params['phone']) != 12:
                return Response({
                    "Error": "Nomer 12 ta raqamdan iborat bo`lishi kerak!"
                })
            otp = random.randint(100000, 999999)
            gkey = generate_key()
            key =  f"{gkey}M{otp}"
            token = code_decode(otp)
            send_sms(params['phone'])
            return Response({
                "otp": otp,
                "otp_token": token,
                "gkey": gkey,
                "key": key
            })

            otp_db = OTP()
            otp_db.token = token
            otp_db.phone = params['phone']
            otp_db.status = "sms_send"
            otp_db.save()

            return Response({
                "otp":otp,
                "otp_token": token,
            })
        elif method == "step.two":
            nott = "otp" if "otp" not in params else "token" if "token" not in params else None
            if nott:
                return Response({
                    "Error": f"params.{nott} to`ldirilmagan"
                })
            otp = OTP.objects.filter(token=params['token']).first()
            if not otp:
                return Response({
                    "Error": f"bunaqa {otp} token topilmadi"
                })
            if otp.expire:
                return Response({
                    "Error": "Bu token eskirgan"
                })
            if code_decode(params['token'])[-7:] != str(params['otp']):
                otp.tried += 1
                otp.save()
                return Response({
                    "Error": "otp raqam xato"
                })
            if not check_otp_expire(otp):
                return Response({
                    "Error": "otp token eskirgan"
                })


            return Response({
                "detoken": code_decode(params['token'], decode=True),
                "token": params['token'],
                "otp": params['otp']
            })



        else:
            return Response({
                "Error": "Bunday method yo`q"
            })


class LikeView(GenericAPIView):
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,

    def post(self, requests):
        data = requests.data
        if 'product_id' not in data or 'status' not in data:
            return Response({
                "Error": "data to'lliq emas"
            })
        prod = Product.objects.filter(pk=data['product_id']).first()
        if not prod:
            return Response({
                "Error": "bunaqa prod yo"
            })
        root = Likes.objects.get_or_create(prod=prod, user=requests.user)[0]
        # default bazadagi holati
        likemi = root.like
        dismi = root.dislike
        if data['status'] == 'like':
            likemi = True
            dismi = False
        elif data['status'] == 'dis':
            likemi = False
            dismi = True

        root.like = likemi
        root.dislike = dismi
        root.save()

        return Response({
            "result": {
                "prod_id": prod.id,
                "user_id": requests.user.id,
                "like": root.like,
                "dis": root.dislike
            }
        })










def format_user(data):
    return OrderedDict([
        ("id", data.id),
        ("first_name", data.first_name),
        ("last_name", data.last_name),
        ("username", data.username),
        ("phone", data.phone),
        ("password", data.password)

    ])


class UserActionsView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

    def get(self, requests):
        ser = self.get_serializer(data={}, instance=requests.user)
        ser.is_valid()

        return Response({
            "user": ser.data
        })

    def post(self, requests):
        data = requests.data
        if "old" not in data or "new" not in data:
            return Response({
                "Error": "data to`liq emas"
            })

        if not requests.user.check_password(data['old']):
            return Response({
                "Error": "parol xato"
            })

        requests.user.set_password(data['new'])
        requests.user.save()

        return Response({
            "Success": "parol o`zgartirildi"
        })
