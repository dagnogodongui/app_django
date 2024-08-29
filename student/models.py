from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=17)
    SEXE_CHOICES = [
        
        ('M', 'Male'),
        
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1 , choices=SEXE_CHOICES)
    matricule = models.CharField(max_length=20, unique=True)
    birthday = models.DateField()
    STATUS_CHOICES = [
        ('6éme', '6éme'),
        ('5éme', '5éme'),
        ('4éme', '4éme'),
        ('3éme', '3eme'),
        ('2nde', '2nde'),
        ('1ére', '1ére'),
        ('Terminale', 'Terminale'),
        ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=7)
    
    
    
