from django.shortcuts import render

# Create your views here.
def index(request):
    context1 ={
        "x": "no ninjas here"
    }
    return render(request,'disappninja_app/index.html',context1)
def ninja(request):
    return render(request,'disappninja_app/ninjas.html')
def show(request, id):
    context = {
        "id" : id ,

      }
    return render(request, 'disappninja_app/index.html',context)
