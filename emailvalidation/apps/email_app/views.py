from django.shortcuts import render,redirect
from .models import Email

# Create your views here.

def index(request):
    return render(request,"email_app/index.html")
def process(request):
    results = Email.objects.emailValidator(request.POST['email'])
    print results
    if results[0] == True:
        context = {
        'succ':request.POST['email'],
        'emails':Email.objects.all()
        }
        return render(request,'email_app/success.html',context)
    if results[0] == False:
        print results[1]
        context ={
        'err' : results[1],
        }
        return render(request,"email_app/index.html",context)
