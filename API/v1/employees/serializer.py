from rest_framework import serializers

from sayt.models import User


class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
