from django.urls import path

from tasks.views import TaskListApi, TaskCreateApi

urlpatterns = [
    path("", TaskListApi.as_view(), name="task-list"),
    path("create/", TaskCreateApi.as_view(), name="task-create"),
]
