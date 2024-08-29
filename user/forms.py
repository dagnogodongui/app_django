from  django import forms
from .models import User

class UserForms(forms.Form):
    pseudo = forms.CharField() 
    password = forms.CharField() 
    

class UserForms(forms.ModelForm):
    class Meta:
         model = User
         fields = ['pseudo','password',]
        
        

    