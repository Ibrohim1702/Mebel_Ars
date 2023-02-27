from collections import OrderedDict

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from API.v1.employees.serializer import CtgSerializer
from sayt.models import Employees


def format(data):
    return OrderedDict([
        ("ism_familya", data.ism_familya),
        ("yoshi", data.yoshi),
        ("lavozimi", data.lavozimi),
        ("salary", data.salary),
        ("city", data.city),
    ])


class EmployeesView(GenericAPIView):
    serializer_class = CtgSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication)

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            emp = Employees.objects.get(pk=pk)
            return Response({
                "item": format(emp)
            })

        emps = Employees.objects.all()
        l = []
        for i in emps:
            l.append(format(i))

        return Response({
            "items": l
        })

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)

        root = serializer.create(serializer.data)

        return Response({
            "result": format(root)
        })

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = Employees.objects.filter(pk=pk).first()

        if not root:
            return Response({
                "Error": "topilmadi"
            })

        serializer = self.get_serializer(data=data, instance=root)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response({
            "result": format(root)
        })

    def delete(self,requests, pk, *args, **kwargs):
        root = Employees.objects.filter(pk=pk).first()
        root.delete()
        return Response({
            "result": f"{pk} Employer deleted"
        })
