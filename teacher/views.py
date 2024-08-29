from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TeacherForms
from .models import Teacher
# Create your views here.
def  index(request): 
    list = Teacher.objects.all()
    context = {'rappe':list}
    return render(request,"teacher/index.html", context)


def add(request):
    if request.method == "POST":
        formulai = TeacherForms(request.POST)
        if formulai.is_valid():
            formulai.save()
    formulai = TeacherForms()
    context = {'formulai': formulai}
    return render(request,"teacher/add.html", context)


def edit(request, id):
    teacher_id = Teacher.objects.get(id=id)
    form = TeacherForms(instance=teacher_id)
    if request.method == "POST":
        form = TeacherForms(request.POST,instance=teacher_id)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
    
    context = {'formulai': form}
    return render(request,"teacher/edit.html",context)


def delete(request, id):
    teacher_id = Teacher.objects.get(id=id)
    teacher_id.delete()
    return redirect('teacher:index')






