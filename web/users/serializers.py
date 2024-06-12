from rest_framework import serializers

from users.models import BaseUser, Employee, Customer


class FilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    is_admin = serializers.BooleanField(required=False, allow_null=True, default=None)
    email = serializers.EmailField(required=False)


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
        )


class UserEmployeeDetailOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "is_active",
            "is_admin",
            "is_superuser",
            "phone_number",
            "photo_url",
        )


class UserCustomerDetailOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "is_active",
            "phone_number",
        )


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


class UserInputSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    middle_name = serializers.CharField(max_length=255, required=False)

    phone_number = serializers.CharField(required=False)


class CustomerInputSerializer(UserInputSerializer):
    pass


class EmployeeInputSerializer(UserInputSerializer):
    photo_url = serializers.URLField()
