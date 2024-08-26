from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  index(request):
    return render(request,"dashboad/index.html")

def connexion(request):
    return render(request,"dashboad/connexion.html")





