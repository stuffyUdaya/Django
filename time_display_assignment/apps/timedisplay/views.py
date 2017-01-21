from django.shortcuts import render,HttpResponse
from datetime import datetime
from time import time

# Create your views here.
def index(request):
    context = {
    "date":datetime.now().strftime("%b %d %Y"),
    "time":datetime.now().strftime("%I:%M %p"),
    "datetime":datetime.now()
    # "time11":datetime.now().strf("%H:%M")
    }


    return render(request,'timedisplay/index.html',context)
