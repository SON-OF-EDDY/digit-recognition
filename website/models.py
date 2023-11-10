from django.db import models

# Create your models here.
class Logger(models.Model):
    error = models.CharField(max_length=20)
    def __str__(self):
        return self.error