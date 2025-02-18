from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    profile = models.ImageField(upload_to='profile/', default='users/user.jpg', blank=True, null=True)

    class Meta:
        db_table = 'user'
        

