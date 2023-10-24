from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# # Create your models here.
#
#
# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)
#     password1 = models.CharField(max_length=128, default='')
#     password2 = models.CharField(max_length=128, default='')
#
#     # Установите related_name для полей groups и user_permissions
#     groups = models.ManyToManyField('auth.Group', related_name='custom_users')
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users_permissions')
#
#     def __str__(self):
#         return self.username
from django.contrib.auth.models import AbstractUser, Permission, Group


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    # Измените related_name для groups и user_permissions
    groups = models.ManyToManyField(Group, verbose_name='Groups', blank=True, related_name='solar_hosting_users')
    user_permissions = models.ManyToManyField(Permission, verbose_name='User permissions', blank=True,
                                              related_name='solar_hosting_users')

    def __str__(self):
        return self.username

