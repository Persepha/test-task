from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from common.models import BaseModel


class BaseUserManager(BUM):
    def create_user(
        self,
        email,
        is_active=True,
        is_admin=False,
        password=None,
        first_name="",
        last_name="",
        middle_name="",
        phone_number="",
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user

    def create_customer(
        self,
        email,
        password=None,
        first_name="",
        last_name="",
        middle_name="",
        phone_number="",
    ):
        user: Customer = self.create_user(
            email=email,
            is_active=True,
            is_admin=False,
            password=password,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
        )

        return user

    def create_employee(
        self,
        email,
        photo_url,
        password=None,
        is_active=True,
        is_admin=True,
        first_name="",
        last_name="",
        middle_name="",
        phone_number="",
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
            photo_url=photo_url,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)

    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin


class Employee(BaseUser):
    user = models.OneToOneField(
        BaseUser, on_delete=models.CASCADE, parent_link=True, related_name="employee"
    )

    photo_url = models.URLField()


class Customer(BaseUser):
    user = models.OneToOneField(
        BaseUser, on_delete=models.CASCADE, parent_link=True, related_name="customer"
    )
