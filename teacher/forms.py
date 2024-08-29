from  django import forms
from .models import Teacher
class TeacherForms(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
   
    sex = forms.CharField()
    birthday = forms.DateField()
    
    course = forms.CharField()
    phone = forms.CharField()
    city = forms.CharField()
    
class TeacherForms(forms.ModelForm):
 class Meta:
        model = Teacher
        fields = ['name','last_name','sex','birthday','course','phone','city']
        
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'}),
                  'phone':forms.NumberInput()}
        
    
    
    


    