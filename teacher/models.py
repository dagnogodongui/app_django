from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=17)
    SEXE_CHOICES = [
        
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1 , choices=SEXE_CHOICES)
    birthday = models.DateField(null = True)
    STATUS_CHOICES = [
        ('Math', 'Math'),
        ('Physique', 'Physique'),
        ('Eps', 'Eps'),
        ('Anglais', 'Anglais'),
        ('SVT', 'SVT'),
        ('Philosophie', 'Philosophie'),
        ('Français', 'Français'),
        ]
    course = models.CharField(max_length=15, choices=STATUS_CHOICES)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=7)
    
    
    
    

