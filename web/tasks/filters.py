import django_filters

from tasks.models import Task


class BaseTaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ("id",)
