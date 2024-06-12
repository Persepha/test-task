from django.db.models.query import QuerySet

from tasks.filters import BaseTaskFilter
from tasks.models import Task


def task_list(*, filters=None) -> QuerySet[Task]:
    filters = filters or {}

    qs = Task.objects.all()

    return BaseTaskFilter(filters, qs).qs
