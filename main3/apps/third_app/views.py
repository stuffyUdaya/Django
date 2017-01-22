from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.
def index(request):
    print (User.objects.all())
    User.objects.create(first_name="Udaya",last_name="Tummala",password="1234qwerty")
    print (User.objects.all())
    u = User.objects.get(id=1)
    print(u.first_name)
    u.first_name = "Joey"
    u.save()
    j = User.objects.get(id=1)
    print(j.first_name)
    print(User.objects.get(first_name = "mike"))
    users = User.objects.raw("select * from third_app_user")
    for user in users:
        print user.first_name
    return HttpResponse("ok")




    print (people[0])
    return render(request,"third_app/index.html")
