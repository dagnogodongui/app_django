from  django import forms
from .models import Student
class EleveForms(forms.Form):
     nom = forms.CharField()
     prenom = forms.CharField()
     sexe = forms.CharField()
     matricule = forms.CharField()
     birthday = forms.DateField()
    
     statut = forms.CharField()
     phone = forms.CharField()
     ville = forms.CharField()
class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','last_name','sex','birthday','status','matricule','phone','city']
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'}),
                  'phone':forms.NumberInput()}
        

    
    
    

    