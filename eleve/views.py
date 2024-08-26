from django.shortcuts import render
from django.http import HttpResponse
from .forms import EleveForms

# Create your views here.
def  index(request):
    return render(request,"eleve/index.html")

def ajout(request):
    if request.method == "POST":
        formulai = EleveForms(request.POST)
        if formulai.is_valid():
            print("form is valid")
            formulai.save()
    print("error")
    formulai = EleveForms()
    context = {'formulai': formulai}
    return render(request,"eleve/ajouter.html", context)

def modifier(request):
    if request.method == "POST":
        formulai = EleveForms(request.POST)
        if formulai.is_valid():
            formulai.save()
    formulai = EleveForms()
    context = {'formulai': formulai}
    return render(request,"eleve/modifie.html",context)


