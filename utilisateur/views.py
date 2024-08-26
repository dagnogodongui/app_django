from django.shortcuts import render
from django.http import HttpResponse
from .forms import UtilisateurForms
# Create your views here.
def  index(request):
    return render(request,"utilisateur/index.html")

def ajout(request):
    if request.method == "POST":
        formulai = UtilisateurForms(request.POST)
        if formulai.is_valid():
            formulai.save()
    formulai = UtilisateurForms()
    context = {'formulai': formulai}
    # tu as trop indenté la ligne juste en la 
    return render(request,"utilisateur/ajouter.html",context)

def modifier(request):
    if request.method == "POST":
        formulai = UtilisateurForms(request.POST)
        if formulai.is_valid():
            formulai.save()
    formulai = UtilisateurForms()
    context = {'formulai': formulai}
    return render(request,"utilisateur/modifie.html",context)
