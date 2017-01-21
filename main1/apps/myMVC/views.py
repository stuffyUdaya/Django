from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'myMVC/index.html')
def show(request):
    print(request.method)

    return render(request,'myMVC/show_users.html')
def create(request):
    if request.method == "POST":
        print ('*'*50)
        print (request.POST)
        print ('*'*50)
        request.session['name'] = request.POST['f_name']
        return redirect('/')
    else:
        return redirect('/')
