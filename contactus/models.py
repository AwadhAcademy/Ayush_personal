from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone=models.IntegerField(default=0)
    message=models.TextField()
    def __str__(self):
        return self.name