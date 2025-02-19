from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True
    )
