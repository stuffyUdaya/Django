from django.shortcuts import render,redirect
from .models import Logins

# Create your views here.

def index(request):
    return render(request,'log_app/index.html')
def process(request):
    # fnameres = Logins.objects1.fnameValidator(request.POST['f_name'])
    results = Logins.objects2.userValidator(request.POST['email'],request.POST['f_name'],request.POST['l_name'],request.POST['password'],request.POST['confpassword'])
    print results
    # print fnameres
    print '$'*35
    print results[0]
    context ={
    'datas': Logins.objects.all()
    }
    # print Logins.objects.email
    print '$'*35
    return render(request,"log_app/index.html",context)
    # if (results[0]==True):
    #     context = {
    #     'succ': results[1]
    #     }
    #     print results[1]
    #     return render(request,"log_app/index.html",context)
    # else:
    #     print results[1]
    #     context = {
    #     'err': results[1]
    #     }
    #     print results[1]
    #     return render(request,"log_app/index.html",context)
    # if fnameres[0] == True :
    #     context = {
    #     'fnamesucc': fnameres[1]
    #     }
    #     print fnameres[1]
    #     return render(request,"log_app/index.html",context)
    # else:
    #     context = {
    #     'fnameerr': fnameres[1]
    #     }
    #     print fnameres[1]
