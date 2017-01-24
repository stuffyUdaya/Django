from django.shortcuts import render,redirect
from .models import Friends,Pairs

# Create your views here.
def index(request):
    context ={
    "friends":Friends.objects.all(),
    "pairs"  :Pairs.objects.all()
    }
    print "*"*50
    return render(request,'pair_app/index.html',context)
def addfriend(request):
    if request.method == 'POST':
        Friends.objects.create(name = request.POST['friend'])

    return redirect('/')
def pairfriend(request):
    if request.method == 'POST':
        pairee = Friends.objects.get(id=request.POST['pairee'] )
        pairer = Friends.objects.get(id=request.POST['pairer'] )
        pairfriends = Pairs.objects.create(friend=pairee, person1 = pairer)
        print pairfriends
        # pairee = Pairs.objects.create(friend = request.POST['pairee'], person1 = request.POST['pairer'])
        # friendid = Friends.objects.filter(name="request.POST['pairee']")
        print '!'*35
        print request.POST['pairee']
        print request.POST['pairer']
        print pairee

        # print friendid

        print Pairs.objects.all()
        return redirect('/')

# Create your views here.
