from django.urls import path

from users.views import UserListApi

urlpatterns = [path("", UserListApi.as_view(), name="user-list")]
