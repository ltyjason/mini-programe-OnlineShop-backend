from rest_framework import serializers

from user.models import WxUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WxUser
        fields = "__all__"