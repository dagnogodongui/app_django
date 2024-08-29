from django.db import models
# Create your models here.
class User(models.Model):
    pseudo = models.CharField(max_length=15) 
    password= models.CharField(max_length=30) 
    create_at = models.DateField(auto_now_add=True)
