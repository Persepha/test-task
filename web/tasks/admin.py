from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from tasks.models import Task
from tasks.services import task_create


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "employee",
        "status",
        "closing_date",
        "report",
    )

    list_select_related = (
        "customer",
        "employee",
    )

    list_filter = ("status",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "customer",
                    "employee",
                    "status",
                    "report",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at", "closing_date")}),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        try:
            task_create(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
