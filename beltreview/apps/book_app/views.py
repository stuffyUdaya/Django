from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .models import User,Book,Join

# Create your views here.
def index(request):
    return render (request, 'book_app/index.html')

def process(request):
    results = User.objects.userValidator(request.POST['name'],request.POST['alias'],request.POST['email'],request.POST['password'],request.POST['confpassword'])
    if results[0]:
        for err in results[1]:
            print err
            messages.error(request,err)
    else:
        request.session ['loggedin'] = results[1].id
        return redirect('/success')
    return redirect('/')
def login(request):
        postData ={
        'email': request.POST['email'],
        'password': request.POST['password']
        }
        results = User.objects.loginValidator(postData)
        if results[0]:
            request.session['loggedin'] = results[1].id
            return redirect('/success')
        else:
            messages.error(request,results[1])
            return redirect('/')
def success(request):
    context = {
        'user' : User.objects.get(id = request.session['loggedin']),
        'books':Book.objects.all()
    }
    return render(request,'book_app/success.html',context)
def addbook(request,id):
    context = {
        'user' : User.objects.get(id = request.session['loggedin']),
    }
    return render(request,'book_app/addbook.html',context)
def add(request,id):
    title = request.POST['title']
    author = request.POST['author']
    review = request.POST['review']
    rating = request.POST['rating']
    user = User.objects.get(id = id)
    book = Book.objects.create(title = title, author = author, review = review, rating = rating, bookuser = user)
    join = Join.objects.create(user= user, review = review, rating = rating, book = book )
    return redirect('/success')
def viewbook(request,id):
    context={
    'book' : Join.objects.get(book_id = id),
    }
    return render(request,"book_app/viewbook.html",context)
