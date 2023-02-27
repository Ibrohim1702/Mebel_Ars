from rest_framework import serializers

from sayt.models import Employees


class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
