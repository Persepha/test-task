from django.urls import path

from users.views import UserListApi, UserMeApi

urlpatterns = [
    path("", UserListApi.as_view(), name="user-list"),
    path("me/", UserMeApi.as_view(), name="user-me"),
]
