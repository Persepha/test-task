from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Employee, Customer
from users.selectors import user_list, user_employee_list
from users.serializers import (
    FilterSerializer,
    UserMeOutputSeriazlier,
    UserOutputSerializer,
    EmployeeInputSerializer,
    CustomerInputSerializer,
    UserEmployeeDetailOutputSerializer,
    UserCustomerDetailOutputSerializer,
)
from users.services import user_create_employee, user_create_customer


class UserEmployeeListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_employee_list(filters=filters_serializer.validated_data)

        data = UserOutputSerializer(users, many=True).data

        return Response(data)


class UserListApi(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        data = UserOutputSerializer(users, many=True).data

        return Response(data)


class UserMeApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserMeOutputSeriazlier(request.user)

        return Response(serializer.data)


class UserEmployeeDetailApi(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, id):
        user = get_object_or_404(Employee, id=id)

        self.check_object_permissions(request, user)

        serializer = UserEmployeeDetailOutputSerializer(user)

        return Response(serializer.data)


class UserCustomerDetailApi(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, id):
        user = get_object_or_404(Customer, id=id)

        self.check_object_permissions(request, user)

        serializer = UserCustomerDetailOutputSerializer(user)

        return Response(serializer.data)


@extend_schema(request=EmployeeInputSerializer)
class UserCreateEmployee(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = EmployeeInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_create_employee(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


@extend_schema(request=CustomerInputSerializer)
class UserCreateCustomer(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = CustomerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = user_create_customer(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)
