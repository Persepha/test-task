from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.selectors import task_list
from tasks.serializers import (
    FilterSerializer,
    TaskOutputSerializer,
    TaskInputSerializer,
)
from tasks.services import task_create
from users.models import Customer


class TaskListApi(APIView):
    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        tasks = task_list(filters=filters_serializer.validated_data)

        data = TaskOutputSerializer(tasks, many=True).data

        return Response(data)


@extend_schema(request=TaskInputSerializer)
class TaskCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TaskInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        created_task = task_create(**serializer.validated_data, customer=user.customer)

        return Response(status=status.HTTP_201_CREATED)
