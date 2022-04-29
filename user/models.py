from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    gender = models.CharField(max_length=10, default='NA')
    phone_number = models.CharField(max_length=20)
