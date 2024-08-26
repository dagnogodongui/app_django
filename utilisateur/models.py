from django.db import models
# Create your models here.
class Utilisateur(models.Model):
    pseudo = models.CharField(max_length=15) 
    mot_de_passe = models.CharField(max_length=30) 
    create_at = models.DateField(auto_now_add=True)
