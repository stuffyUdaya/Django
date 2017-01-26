from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def index(request):


    return render(request,'register_app/index.html')
def process(request):
    results = User.objects.userValidator(request.POST['email'],request.POST['f_name'],request.POST['l_name'],request.POST['password'],request.POST['confpassword'])
    if not results[0]:
        context = {
            'errors' :results[1]
        }
        print results
        return render(request,'register_app/index.html',context)
    else:
        print "*"*50
        print results
        return redirect('/success')
def success(request):
    return render(request,'register_app/success.html')
def login(request):
    email = request.POST['email']
    pwd = request.POST['password']
                

    # # print fnameres
    # print '$'*35
    # print results[0]
    # context ={
    # 'datas': Logins.objects.all()
    # }
    # print Logins.objects.email
    print '$'*35
    return render(request,"register_app/index.html")
    # ,context)
