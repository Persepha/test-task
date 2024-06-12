from django.contrib import admin, messages
from django.core.exceptions import ValidationError

from users.models import BaseUser, Employee, Customer
from users.services import user_create, user_create_employee, user_create_customer


@admin.register(Employee)
class UserEmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_admin",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
        "first_name",
        "last_name",
        "middle_name",
        "phone_number",
        "photo_url",
    )

    list_filter = ("is_active", "is_admin", "is_superuser")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "photo_url",
                    "first_name",
                    "last_name",
                    "middle_name",
                    "phone_number",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    search_fields = ("email",)

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        try:
            user_create_employee(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)


@admin.register(Customer)
class UserEmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_active",
        "created_at",
        "updated_at",
        "first_name",
        "last_name",
        "middle_name",
        "phone_number",
    )

    list_filter = ("is_active",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "middle_name",
                    "phone_number",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    search_fields = ("email",)

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        try:
            user_create_customer(**form.cleaned_data)
        except ValidationError as exc:
            self.message_user(request, str(exc), messages.ERROR)
