from django.db.models.query import QuerySet

from tasks.filters import BaseTaskFilter
from tasks.models import Task
from users.models import Customer


def task_list(*, filters=None) -> QuerySet[Task]:
    filters = filters or {}

    qs = Task.objects.all()

    return BaseTaskFilter(filters, qs).qs


def customer_task_list(*, customer: Customer, filters=None) -> QuerySet[Task]:
    filters = filters or {}

    qs = Task.objects.filter(customer=customer)

    return BaseTaskFilter(filters, qs).qs
