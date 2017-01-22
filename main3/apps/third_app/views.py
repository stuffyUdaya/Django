from django.shortcuts import render
from .models import People

# Create your views here.
def index(request):
    People.objects.create(first_name="Udaya",last_name="Tummala")
    people = People.objects.all()
    print (people[0])
    return render(request,"third_app/index.html")
