from datetime import date
from typing import Tuple

from django.core.exceptions import ValidationError
from django.db import transaction
from django.utils import timezone

from common.services import model_update, is_string_blank
from tasks.models import Task
from users.models import Customer, Employee


def task_create(
    *,
    status: str = Task.PENDING,
    description: str = "",
    customer: Customer,
    employee: Employee | None = None,
    closing_date: date | None = None,
    report: str = ""
) -> Task:
    task = Task(
        customer=customer,
        employee=employee,
        report=report,
        status=status,
        closing_date=closing_date,
        description=description,
    )
    task.full_clean()
    task.save()

    return task


def task_set_employee(*, employee: Employee, task: Task) -> Task:
    task.employee = employee
    task.status = Task.IN_PROCESS

    task.full_clean()
    task.save()

    return task


@transaction.atomic
def task_update(*, task: Task, data) -> Tuple[Task, bool]:
    if task.status == Task.DONE:
        raise ValidationError("Cannot change a task with status = Done")

    non_side_effect_fields = ["description", "report", "status"]

    task, has_updated = model_update(
        instance=task,
        fields=non_side_effect_fields,
        data=data,
    )

    return task, has_updated


def task_close(*, task: Task, report: str = "") -> Task:
    if is_string_blank(task.report):
        raise ValidationError("Cannot close a task without report")

    task.report = report
    task.closing_date = timezone.now()
    task.status = Task.DONE

    task.full_clean()
    task.save()

    return task
