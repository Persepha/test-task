from users.models import BaseUser, Employee, Customer


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
    phone_number: str = "",
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


def user_create_employee(
    *,
    email: str,
    password: str | None = None,
    first_name: str = "",
    last_name: str = "",
    middle_name: str = "",
    phone_number: str = "",
    photo_url: str,
) -> Employee:
    user = Employee.objects.create_employee(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        phone_number=phone_number,
        photo_url=photo_url,
    )

    return user


def user_create_customer(
    *,
    email: str,
    password: str | None = None,
    first_name: str = "",
    last_name: str = "",
    middle_name: str = "",
    phone_number: str = "",
) -> Customer:
    user = Customer.objects.create_customer(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        phone_number=phone_number,
    )

    return user
