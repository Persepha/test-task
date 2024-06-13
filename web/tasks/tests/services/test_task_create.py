from django.test import TestCase

from tasks.models import Task
from tasks.services import task_create
from users.models import Customer


class TaskCreateTests(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(email="test@test.com")

    def test_creating_task(self):
        self.assertEqual(0, Task.objects.count())
        created_task = task_create(customer=self.customer)
        self.assertEqual(1, Task.objects.count())
        self.assertEqual(created_task, Task.objects.first())
        self.assertEqual(Task.PENDING, Task.objects.first().status)
        self.assertEqual(self.customer, Task.objects.first().customer)
        self.assertIsNone(Task.objects.first().employee)
