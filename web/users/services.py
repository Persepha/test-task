from typing import Optional

from users.models import BaseUser


def user_create(
    *,
    email: str,
    is_active: bool = True,
    is_admin: bool = False,
    is_superuser: bool = False,
    password: str | None = None,
    first_name: str = "",
    last_name: str = "",
    middle_name: str = "",
    phone_number: str = ""
) -> BaseUser:
    user = BaseUser.objects.create_user(
        email=email,
        is_active=is_active,
        is_admin=is_admin,
        password=password,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        phone_number=phone_number,
    )

    return user
