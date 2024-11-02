from django.db import models

# Create your models here.
 

class SorryCount(models.Model):
    user = models.CharField(max_length=10, unique=True)  # Either "Vika" or "Eskil"
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}: {self.count} apologies"
