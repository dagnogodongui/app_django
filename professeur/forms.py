from  django import forms
from .models import Professeur
class ProfesseurForms(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
   
    sexe = forms.CharField()
    date_de_naissance = forms.DateField()
    
    statut = forms.CharField()
    telephone = forms.CharField()
    ville = forms.CharField()
    
class ProfesseurForms(forms.ModelForm):
 class Meta:
        model = Professeur
        fields = ['nom','prenom','sexe','date_de_naissance','matiere','telephone','ville']
        
    
    
    


    