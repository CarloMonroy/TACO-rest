from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    location = models.URLField()

    def __str__(self):
        return self.name

