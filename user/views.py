from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForms
from .models import User
from django.contrib.auth.models import User as  SuperUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
def  index(request):
    list = User.objects.all()
    context = {'dork':list}
    return render(request,"user/index.html",context)

def add(request):
     if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if not username or not password:
            return render(request, 'html/signin.html')
        
        user = User(username=username)
        user.save()
        user.set_password(user.password)
        user.save()
        login(request,user)
        return redirect("authApp:Home")
     
        if request.method == "POST":
        
            formulai = UserForms(request.POST)
        if  formulai.is_valid():
            formulai.save() 
            formulai = UserForms()
        context = {'formulai': formulai} 
        return render(request,"user/add.html",context)

def edit(request, id):
    user_id = User.objects.get(id=id)
    if request.method == "POST":
        form = UserForms(request.POST,instance=user_id)
        if form.is_valid():
           form.save()
           return redirect('user:index')
    form = UserForms(instance=user_id)
    context = {'formulai': form}
    return render(request,"user/edit.html",context)


#def delete(request,id):
    #user_id = Teacher.objects.get(id=id)
    #user_id.delete()
    #return redirect('user:index')

