from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from tasks.models import Task


class IsUserHasAccessToViewTask(permissions.BasePermission):
    """
    Check If authorized user can get task detail
    """

    def has_object_permission(self, request: Request, view: APIView, obj: Task) -> bool:
        if not request.user:
            return False

        if request.user.is_superuser:
            return True

        if bool(
            hasattr(request.user, "customer") and request.user.customer == obj.customer
        ):
            return True

        if bool(
            hasattr(request.user, "employee")
            and (request.user.employee == obj.employee or obj.employee is None)
        ):
            return True

        return False


class IsUserHasPermissionToAssignTask(permissions.BasePermission):
    """
    Check If authorized user can assign task to himself
    """

    def has_object_permission(self, request: Request, view: APIView, obj: Task) -> bool:
        if not request.user:
            return False

        if bool(
            hasattr(request.user, "employee")
            and (request.user.employee == obj.employee or obj.employee is None)
        ):
            return True

        return False


class IsCustomer(permissions.BasePermission):
    """
    Check If authorized user is customer
    """

    def has_permission(self, request, view):
        return bool(request.user and hasattr(request.user, "customer"))


class IsSuperUser(permissions.BasePermission):
    """
    Check If superusers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
