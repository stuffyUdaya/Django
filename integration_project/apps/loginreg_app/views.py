from django.shortcuts import render,redirect
from .models import User
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def index(request):

    print User.objects.all()
    return render(request,'loginreg_app/index.html')
def process(request):
    results = User.objects.userValidator(request.POST['email'],request.POST['f_name'],request.POST['l_name'],request.POST['password'],request.POST['confpassword'])
    if results[0]:
        for err in results[1]:
            print err
            messages.error(request,err)
    else:
        request.session ['loggedin'] = results[1].id
        return redirect(reverse('courses:courses_index'))
    return redirect(reverse('users:lreg_index'))
def success(request):

    context={
    'user': User.objects.filter(id = request.session['loggedin'])
    }
    return render(request,'loginreg_app/success.html',context)
def login(request):
    postData ={
      'email': request.POST['email'],
      'password': request.POST['password']
    }
    results = User.objects.loginValidator(postData)
    if results[0]:
        request.session['loggedin'] = results[1].id
        return redirect (reverse('users:success'))
    else:
        messages.error(request,results[1])
        return redirect(reverse('users:lreg_index'))

def logout(request):
    return redirect(reverse('users:lreg_index'))
