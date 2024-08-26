from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProfesseurForms
# Create your views here.
def  index(request):
    return render(request,"professeur/index.html")

def ajout(request):
    if request.method == "POST":
        formulai = ProfesseurForms(request.POST)
        if formulai.is_valid():
            formulai.save()
    formulai = ProfesseurForms()
    context = {'formulai': formulai}
    return render(request,"professeur/ajouter.html", context)

def modifier(request):
    if request.method == "POST":
        formulai = ProfesseurForms(request.POST)
        if formulai.is_valid():
            formulai.save()
    formulai = ProfesseurForms()
    context = {'formulai': formulai}
    return render(request,"professeur/modifie.html",context)






