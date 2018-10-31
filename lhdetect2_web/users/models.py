from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    organization = models.CharField(max_length=500)
    division = models.CharField(max_length=500)
    sharing = models.BooleanField(default=True)

    def __str__(self):
        return self.email
