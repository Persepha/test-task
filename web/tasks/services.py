from datetime import date

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
