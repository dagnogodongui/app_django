from django.urls import path
from . import views 
app_name="eleve"
urlpatterns = [
    path('',views.index,name ='index'),
    path('ajouter/',views.ajout,name = 'add'),
     path('modifier/',views.modifier, name ='edit'),
]