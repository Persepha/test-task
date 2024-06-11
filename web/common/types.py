from typing import TypeVar

from django.db import models

# Generic type for a django model
DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)
