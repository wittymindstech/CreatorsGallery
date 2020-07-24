from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title