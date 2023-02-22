from django.contrib.auth.models import Permission, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from base.db import ExtraModelHelper


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):

        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=128, null=True, blank=True,  default="Qo`ysuluv")
    last_name = models.CharField(max_length=128, null=True, blank=True, default="Jakuy" )
    email = models.EmailField(max_length=128,null=True, blank=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=15, null=True, blank=True)
    company = models.CharField(max_length=128, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    bio = models.CharField(max_length=256, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


def __str__(self):
    return self.username



class   ServerToken(models.Model):
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=128)
    key = models.CharField(max_length=256)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    token = models.TextField()


class OTP(models.Model, ExtraModelHelper):
    token = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    expire = models.BooleanField(default=False)
    tried = models.IntegerField()
    status = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    def save(self, *args, **kwargs):
        if self.tried == 3:
             self.expire = True
        return super(OTP, self).save(*args, **kwargs)

    @classmethod
    def get_or_none(cls, token):
        pass




