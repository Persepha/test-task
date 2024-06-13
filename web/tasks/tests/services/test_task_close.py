from django.core.exceptions import ValidationError
from django.test import TestCase

from tasks.models import Task
from tasks.services import task_close
from users.models import Employee, Customer


class TaskCloseTests(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(email="test@test.com")
        self.employee1 = Employee.objects.create_employee(
            email="empl@test.com", photo_url="http://empl@test.com"
        )
        self.task1 = Task.objects.create(
            customer=self.customer, employee=self.employee1, report="test"
        )
        self.task2 = Task.objects.create(
            customer=self.customer, employee=self.employee1
        )

    def test_task_close_with_report(self):
        self.assertEqual(Task.PENDING, Task.objects.get(pk=self.task1.id).status)
        updated_task = task_close(task=self.task1)
        self.assertEqual(Task.DONE, Task.objects.get(pk=self.task1.id).status)

    def test_task_close_without_report(self):
        self.assertEqual(Task.PENDING, Task.objects.get(pk=self.task2.id).status)

        with self.assertRaises(
            ValidationError, msg="Cannot close a task without report"
        ):
            updated_task = task_close(task=self.task2)

        self.assertEqual(Task.PENDING, Task.objects.get(pk=self.task2.id).status)
