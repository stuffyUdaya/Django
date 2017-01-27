from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Courses
import datetime

# Create your views here.

def index(request):
    context={
    "courses":Courses.objects.all()
    }
    return render(request,"courses_app/index.html",context)
def add(request):
    if request.method == 'POST':
        Courses.objects.create(name=request.POST['name'], desc=request.POST['desc'], created_at=datetime.datetime.now())

    return redirect(reverse('courses:courses_index'))
def remove(request,id):
    context1 ={
        "deletecourses":Courses.objects.get(id=id)
    }

    print '#'* 35


    return render(request,"courses_app/delete.html",context1)
def delete(request,id):
    if request.method == "POST":
        Courses.objects.filter(id=id).delete()
        return redirect(reverse('courses:courses_index'))
