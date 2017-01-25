from django.shortcuts import render,redirect,HttpResponse
from .models import Email

# Create your views here.

def index(request):
    return render(request,"login_app/index.html")
def process(request):
    results = Email.objects.emailValidator(request.POST['email'])
    print results

    if (results[0]==True):
        context = {
        'Succ':results[1]
        }
        print results[1]
        return render(request,"login_app/index.html",context)
    else:
        print results[1]
        context = {
        'ERR': results[1]
        }
        return render(request,"login_app/index.html",context)
def success(request):
    return redirect('/')





    # User.userManager.login("speros@codingdojo.com","Speros")
    # return HttpResponse(User.userManager.login("speros@codingdojo.com","Speros"))
    #   print("Running index method, calling out to User.")


# # DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
#       print (type(user))
#       if 'error' in user:
#           pass
#       if 'theuser' in user:
#           pass
