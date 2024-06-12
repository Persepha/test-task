from django.db import models

from common.models import BaseModel
from users.models import Customer, Employee


class Task(BaseModel):
    PENDING = "P"
    IN_PROCESS = "IP"
    DONE = "D"
    TASK_STATUS_CHOICES = {
        PENDING: "pending",
        IN_PROCESS: "in process",
        DONE: "done",
    }

    description = models.TextField(blank=True)

    customer = models.ForeignKey(
        Customer, related_name="tasks", on_delete=models.CASCADE
    )
    employee = models.ForeignKey(
        Employee, related_name="tasks", on_delete=models.SET_NULL, null=True, blank=True
    )

    status = models.CharField(
        max_length=2, choices=TASK_STATUS_CHOICES, default=PENDING
    )
    closing_date = models.DateField(blank=True, null=True)
    report = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Task {self.id} from {self.customer}"
