from django.db import models
from django.db.models.base import Model

# Create your models here.


class UserProfile(models.Model):
    image = models.FileField(upload_to="images")