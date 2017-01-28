from django.shortcuts import render,redirect
from .models import User,Trip
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def index(request):
    # trip =Trip.objects.all()
    # # print trip[11].userid
    # # tripuser= trip[10].id
    # # print tripuser
    # print User.objects.all().delete()
    # print Trip.objects.all().delete()
    return render(request,'travel_app/index.html')
def process(request):
    results = User.objects.userValidator(request.POST['name'],request.POST['u_name'],request.POST['password'],request.POST['confpassword'])
    if results[0]:
        for err in results[1]:
            print err
            messages.error(request,err)
    else:
        request.session ['loggedin'] = results[1].id
        return redirect('/success')
    return redirect('/')
def success(request):
    user = User.objects.get(id=id)
    context={
    'user':  User.objects.filter(id = request.session['loggedin']),
    'trips': Trip.objects.filter(id = request.session['loggedin'] ),
    'views': Trip.objects.all().exclude(userid = request.session['loggedin'])
    }
    return render(request,'travel_app/success.html',context)
def login(request):
    postData ={
      'u_name': request.POST['u_name'],
      'password': request.POST['password']
    }
    results = User.objects.loginValidator(postData)
    if results[0]:
        request.session['loggedin'] = results[1].id
        return redirect('/success')
    else:
        messages.error(request,results[1])
        return redirect('/')
def addtravelplan(request,id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request,'travel_app/addtravel.html',context)
def addtrip(request,id):
    print '*'*34
    user = User.objects.get(id=id)
    userid =  user.id
    print userid

    print '*'*34

    trip= Trip.objects.create(destination = request.POST['destination'], description = request.POST['description'],datefrom = request.POST['datefrom'], dateto = request.POST['dateto'],userid = userid )


    return redirect('/success')
def viewtrip(request,id):
    # context = {
    #  'view' :
    # }
    return render(request,'travel_app/viewtravel.html')

def logout(request):
    return redirect('/')
