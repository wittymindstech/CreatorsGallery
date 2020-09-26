# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title