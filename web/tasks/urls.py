from django.urls import path

from tasks.views import TaskListApi, TaskCreateApi, TaskDetailApi, TaskSetEmployee

urlpatterns = [
    path("", TaskListApi.as_view(), name="task-list"),
    path("create/", TaskCreateApi.as_view(), name="task-create"),
    path("<int:id>/", TaskDetailApi.as_view(), name="task-detail"),
    path("<int:id>/setemployee/", TaskSetEmployee.as_view(), name="task-setemployee"),
]
