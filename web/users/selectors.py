from django.db.models.query import QuerySet

from users.filters import BaseUserFilter
from users.models import BaseUser


def user_list(*, filters=None) -> QuerySet[BaseUser]:
    filters = filters or {}

    qs = BaseUser.objects.all()

    return BaseUserFilter(filters, qs).qs
