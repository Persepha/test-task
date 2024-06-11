from rest_framework import serializers

from users.models import BaseUser


class FilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
    email = serializers.EmailField(required=False)


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ("id", "email", "is_admin")


class UserMeOutputSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = (
            "id",
            "email",
            "is_active",
            "is_admin",
            "is_superuser",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
        )
