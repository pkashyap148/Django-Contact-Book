from django.db import models

# Create your models here.
class directory(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name