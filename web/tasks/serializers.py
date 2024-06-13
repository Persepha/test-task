from rest_framework import serializers

from tasks.models import Task
from users.serializers import UserOutputSerializer


class TaskOutputSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display", read_only=True)
    customer = UserOutputSerializer(read_only=True)
    employee = UserOutputSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "customer",
            "status",
            "employee",
            "report",
            "closing_date",
            "description",
        )


class TaskInputSerializer(serializers.Serializer):
    description = serializers.CharField(required=False)


class TaskUpdateInputSerializer(TaskInputSerializer):
    report = serializers.CharField(required=False)
    status = serializers.CharField(required=False)


class FilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
