from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from utils.models import BaseModel
from django.utils.html import format_html


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    user_name = models.CharField(max_length=150, unique=True, db_index=True)
    first_name = models.CharField(max_length=150, blank=True, db_index=True)
    last_name = models.CharField(max_length=150, blank=True)
    date_of_birth = models.DateField(auto_now_add=False, editable=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='users', null=True, blank=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def change_button(self):
        return format_html('<a class="btn" href="/admin/users/models/{}/edit/">Edit</a>', self.id)

    def delete_button(self):
        return format_html('<a class="btn" href="/admin/users/models/{}/delete/">Delete</a>',self.id)

    def __str__(self):
        return self.user_name


class BlockedUser(BaseModel):
    user_id = models.ForeignKey(NewUser, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    blocked_id = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user_id.user_name
