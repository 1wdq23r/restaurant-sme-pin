from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.name
