from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import EmailField, BooleanField

from core.managers import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    email = EmailField(unique=True)
    USERNAME_FIELD = 'email'
    objects = AccountManager()
