from django.shortcuts import render,redirect
# from session import session

# Create your views here.
def index(request):
    print "*"*50
    return render(request,'survey_app/index.html')
def showuser(request):
    if request.method =='POST':

        request.session['fname'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment']  = request.POST['comment']

        # request.session['randomword']= request.session['randomword']+1

        if 'counter' in request.session:
           request.session['counter'] = request.session['counter'] + 1
        #    return render(request,'survey_app/showusers.html')
        else:
           request.session['counter'] = 1

        return render(request,'survey_app/showusers.html')

    else:
        return redirect('/')

def back(request):
    # request.session['number'] += 1
    return redirect('/')
