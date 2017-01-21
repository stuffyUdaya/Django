from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    context={
        'randomword': get_random_string(length=16)


    }


    return render(request,'randomgen/index.html',context)
def newword(request):
    request.session['number'] = request.session['number']+1
    return redirect('/')
def clear(request):
    request.session['number'] = 0
    return redirect('/')
