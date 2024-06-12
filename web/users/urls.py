from django.urls import path

from users.views import (
    UserEmployeeListApi,
    UserMeApi,
    UserCreateEmployee,
    UserCreateCustomer,
    UserListApi,
    UserEmployeeDetailApi,
    UserCustomerDetailApi,
)

urlpatterns = [
    path("", UserEmployeeListApi.as_view(), name="user-employee-list"),
    path("all/", UserListApi.as_view(), name="user-list"),
    path("me/", UserMeApi.as_view(), name="user-me"),
    path("create_employee/", UserCreateEmployee.as_view(), name="user-create-employee"),
    path("create_customer/", UserCreateCustomer.as_view(), name="user-create-customer"),
    path(
        "employee/<int:id>/",
        UserEmployeeDetailApi.as_view(),
        name="user-employee-detail",
    ),
    path(
        "customer/<int:id>/",
        UserCustomerDetailApi.as_view(),
        name="user-customer-detail",
    ),
]
