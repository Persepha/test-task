from django.core.exceptions import ValidationError
from django.test import TestCase

from tasks.models import Task
from tasks.services import task_update
from users.models import Employee, Customer


class TaskUpdateTests(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(email="test@test.com")
        self.employee1 = Employee.objects.create_employee(
            email="empl@test.com", photo_url="http://empl@test.com"
        )
        self.task1 = Task.objects.create(
            customer=self.customer, employee=self.employee1
        )
        self.task2 = Task.objects.create(
            customer=self.customer, employee=self.employee1, status=Task.DONE
        )

    def test_task_update(self):
        self.assertEqual(Task.PENDING, Task.objects.get(pk=self.task1.id).status)
        data = {"status": "IP", "report": "test"}
        updated_task, is_updated = task_update(task=self.task1, data=data)
        self.assertEqual(is_updated, True)
        self.assertEqual(updated_task, Task.objects.get(pk=self.task1.id))
        self.assertEqual(Task.IN_PROCESS, Task.objects.get(pk=self.task1.id).status)

    def test_task_update_when_task_closed(self):
        self.assertEqual(Task.DONE, Task.objects.get(pk=self.task2.id).status)
        data = {"status": "IP", "report": "test"}

        with self.assertRaises(
            ValidationError, msg="Cannot change a task with status = Done"
        ):
            updated_task, is_updated = task_update(task=self.task2, data=data)
            self.assertEqual(is_updated, False)
