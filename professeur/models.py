from django.db import models

# Create your models here.
class Professeur(models.Model):
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=17)
    SEXE_CHOICES = [
        
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    sexe = models.CharField(max_length=1 , choices=SEXE_CHOICES)
    date_de_naissance = models.DateField(null = True)
    STATUS_CHOICES = [
        ('Math', 'Math'),
        ('Physique', 'Physique'),
        ('Eps', 'Eps'),
        ('Anglais', 'Anglais'),
        ('SVT', 'SVT'),
        ('Philosophie', 'Philosophie'),
        ('Français', 'Français'),
        ]
    matiere = models.CharField(max_length=15, choices=STATUS_CHOICES)
    telephone = models.CharField(max_length=10)
    ville = models.CharField(max_length=7)
    
    
    
    

