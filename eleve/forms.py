from  django import forms
from .models import Eleve
# class EleveForms(forms.Form):
#     nom = forms.CharField()
#     prenom = forms.CharField()
#     sexe = forms.CharField()
#     matricule = forms.CharField()
#     date_de_naissance = forms.DateField()
    
#     statut = forms.CharField()
#     telephone = forms.CharField()
#     ville = forms.CharField()
class EleveForms(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom','prenom','sexe','date_de_naissance','classe','matricule','telephone','ville']
        

    
    
    

    