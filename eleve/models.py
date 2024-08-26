from django.db import models

# Create your models here.
class Eleve(models.Model):
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=17)
    SEXE_CHOICES = [
        
        ('M', 'Masculin'),
        
        ('F', 'Féminin'),
    ]
    sexe = models.CharField(max_length=1 , choices=SEXE_CHOICES)
    matricule = models.CharField(max_length=20, unique=True)
    date_de_naissance = models.DateField()
    STATUS_CHOICES = [
        ('6', '6éme'),
        ('5', '5éme'),
        ('4', '4éme'),
        ('3', '3eme'),
        ('2', '2nde'),
        ('1', '1ére'),
        ('Tle', 'Terminale'),
        ]
    classe = models.CharField(max_length=3, choices=STATUS_CHOICES)
    telephone = models.CharField(max_length=10)
    ville = models.CharField(max_length=7)
    
    
    
