from django.test import TestCase

from tasks.models import Task
from tasks.services import task_set_employee
from users.models import Employee, Customer


class TaskSetEmployeeTests(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(email="test@test.com")
        self.task1 = Task.objects.create(customer=self.customer)
        self.employee1 = Employee.objects.create_employee(
            email="empl@test.com", photo_url="http://empl@test.com"
        )

    def test_task_set_employee(self):
        self.assertEqual(1, Task.objects.count())

        self.assertIsNone(self.task1.employee)
        updated_task = task_set_employee(employee=self.employee1, task=self.task1)
        self.assertEqual(1, Task.objects.count())
        self.assertEqual(self.employee1, Task.objects.first().employee)
        self.assertEqual(self.customer, Task.objects.first().customer)
