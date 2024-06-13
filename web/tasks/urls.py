from django.urls import path

from tasks.views import (
    TaskListApi,
    TaskCreateApi,
    TaskDetailApi,
    TaskSetEmployee,
    TaskListForCustomerApi,
    TaskUpdateApi,
)

urlpatterns = [
    path("", TaskListApi.as_view(), name="task-list"),
    path("create/", TaskCreateApi.as_view(), name="task-create"),
    path(
        "created_tasks/",
        TaskListForCustomerApi.as_view(),
        name="task-created_by_customer",
    ),
    path("<int:id>/", TaskDetailApi.as_view(), name="task-detail"),
    path("<int:id>/update/", TaskUpdateApi.as_view(), name="task-update"),
    path("<int:id>/setemployee/", TaskSetEmployee.as_view(), name="task-setemployee"),
]
