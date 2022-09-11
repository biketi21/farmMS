from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class Farmer(models.Model):
    First_Name = models.CharField(max_length=50)
    SurName    = models.CharField(max_length=50)
    Farm_ID    = models.ForeignKey(Account, on_delete=models.PROTECT)
    ID_Number  = models.IntegerField(unique=True)
    Phone_No   = models.CharField(max_length=20)
    Farm_Name  = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return str(self.First_Name + ' ' + self.SurName)

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date    = models.DateTimeField()

    def __str__(self):
        return f'{self.title}: due{self.due_date}'

    class Meta:
        ordering = ['due_date']
