from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.permissions import (
    IsUserHasAccessToViewTask,
    IsUserHasPermissionToAssignTask,
    IsCustomer,
    IsUserHasPermissionToChangeTask,
    IsSuperUser,
)
from tasks.selectors import task_list, customer_task_list
from tasks.serializers import (
    FilterSerializer,
    TaskOutputSerializer,
    TaskInputSerializer,
    TaskUpdateInputSerializer,
    TaskCloseInputSerializer,
)
from tasks.services import task_create, task_set_employee, task_update, task_close
from users.models import Customer


class TaskListApi(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        tasks = task_list(filters=filters_serializer.validated_data)

        data = TaskOutputSerializer(tasks, many=True).data

        return Response(data)


class TaskListForCustomerApi(APIView):
    permission_classes = (IsCustomer,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        user = self.request.user

        tasks = customer_task_list(
            filters=filters_serializer.validated_data, customer=user.customer
        )

        data = TaskOutputSerializer(tasks, many=True).data

        return Response(data)


class TaskDetailApi(APIView):
    permission_classes = (IsUserHasAccessToViewTask,)

    def get(self, request, id):
        task = get_object_or_404(Task, id=id)

        self.check_object_permissions(request, task)

        serializer = TaskOutputSerializer(task)

        return Response(serializer.data)


@extend_schema(request=TaskInputSerializer)
class TaskCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TaskInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        created_task = task_create(**serializer.validated_data, customer=user.customer)

        return Response(status=status.HTTP_201_CREATED)


class TaskSetEmployee(APIView):
    permission_classes = (IsUserHasPermissionToAssignTask,)

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)

        self.check_object_permissions(request, task)

        user = self.request.user

        updated_task = task_set_employee(task=task, employee=user.employee)

        return Response(status=status.HTTP_200_OK)


@extend_schema(request=TaskUpdateInputSerializer)
class TaskUpdateApi(APIView):
    permission_classes = (IsUserHasPermissionToChangeTask | IsSuperUser,)

    def post(self, request, id):
        serializer = TaskUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = get_object_or_404(Task, id=id)

        self.check_object_permissions(request, task)

        updated_task, _ = task_update(task=task, data=serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


@extend_schema(request=TaskCloseInputSerializer)
class TaskCloseApi(APIView):
    permission_classes = (IsUserHasPermissionToChangeTask | IsSuperUser,)

    def post(self, request, id):
        serializer = TaskCloseInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = get_object_or_404(Task, id=id)
        self.check_object_permissions(request, task)

        updated_task = task_close(task=task, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)
