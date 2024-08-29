from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForms
from .models import  Student


# Create your views here.
def  index(request):
    list = Student.objects.all()
    context = {'elf':list}
    return render(request,"student/index.html",context)


def add(request):
    if request.method == "POST":
        formulai = StudentForms(request.POST)
        if formulai.is_valid():
            print("form is valid")
            formulai.save()
    formulai = StudentForms()
    context = {'formulai': formulai}
    return render(request,"student/add.html", context)


def edit(request,id):
    student_id = Student.objects.get(id=id)
    form = StudentForms(instance=student_id)
    if request.method == "POST":
        form = StudentForms(request.POST, instance=student_id)
        #formulai = StudentForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student:index')
    formulai = StudentForms()
    context = {'formulai': form}
    return render(request,"student/edit.html",context)


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student:index')



