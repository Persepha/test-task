from django.db.models.query import QuerySet

from users.filters import BaseUserFilter
from users.models import BaseUser, Employee


def user_list(*, filters=None) -> QuerySet[BaseUser]:
    filters = filters or {}

    qs = BaseUser.objects.all().select_related("customer", "employee")

    return BaseUserFilter(filters, qs).qs


def user_employee_list(*, filters=None) -> QuerySet[BaseUser]:
    filters = filters or {}

    qs = Employee.objects.all()

    return BaseUserFilter(filters, qs).qs
