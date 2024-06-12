# Generated by Django 5.0 on 2024-06-12 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
        ("users", "0002_customer_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="closing_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tasks",
                to="users.employee",
            ),
        ),
    ]
