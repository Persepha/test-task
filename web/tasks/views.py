from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.permissions import IsUserHasAccessToViewTask, IsUserHasPermissionToAssignTask
from tasks.selectors import task_list
from tasks.serializers import (
    FilterSerializer,
    TaskOutputSerializer,
    TaskInputSerializer,
)
from tasks.services import task_create, task_set_employee
from users.models import Customer


class TaskListApi(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        tasks = task_list(filters=filters_serializer.validated_data)

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
    # permission_classes = (IsSuperUser | (IsAdminUser & (IsTaskWithoutEmployee | IsOwner)),)

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)

        self.check_object_permissions(request, task)

        user = self.request.user

        updated_task = task_set_employee(task=task, employee=user.employee)

        return Response(status=status.HTTP_200_OK)
