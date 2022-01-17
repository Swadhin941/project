from django.db import models

# Create your models here.
class accounts(models.Model):
    District= models.CharField(max_length=200)
    Bedrooms= models.CharField(max_length=200)
    Price= models.CharField(max_length=200)
    Description= models.TextField()