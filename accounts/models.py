from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError("The given username is not valid")
        email= self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True,
                            is_staff=is_staff, is_superuser=is_superuser,date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(self, username, email, password,is_active=True,is_staff=False,is_superuser=False,
         **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username,email,password,is_active=True,
        is_staff=True,is_superuser=True, **extra_fields)

        return user


# class User(AbstractBaseUser, PermissionMixin):

