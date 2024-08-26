from  django import forms
from .models import Utilisateur

class UtilisateurForms(forms.Form):
    pseudo = forms.CharField() 
    mot_de_passe = forms.CharField() 
    

class UtilisateurForm(forms.ModelForm):
    class Meta:
         model = Utilisateur
         fields = ['pseudo','mot_de_passe',]
        
        

    