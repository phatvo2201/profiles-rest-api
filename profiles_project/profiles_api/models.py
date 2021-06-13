from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('User must have email address')
        email = self.nomalize_email(email)

        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self.__db)
        return user
    def create_superuser(self,email,name,password):
        user.create_user(email,name,password)
        user.is_Superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """database model for usr in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELD='name'
    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email
