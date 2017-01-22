from django.shortcuts import render,redirect
import random
import math
from datetime import datetime

# Create your views here.
def index(request):
    if request.session.get('gold')== None :
        request.session['gold'] =0
        request.session['activities'] = []
    return render(request,'ninjagold_app/index.html')
def process(request):
    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            farmgold = random.randint(10,20)
            location = "farm"
            request.session['color'] = "earned"
            now = str(datetime.now())
            string = ("Earned " +str(farmgold) + " golds from the " +location+ " " +now)
            print "*"* 30
            print request.session['string']
            request.session['activities'].insert(0, {'string':string})
            print "*"*30
            print request.session['activities']
            request.session['gold'] += farmgold
        elif request.POST['building'] == 'cave':
            request.session['color'] ="earned"
            location = "cave"
            cavegold = random.randint(5,10)
            now = str(datetime.now())
            string = ("Earned " +str(cavegold) + " golds from the " +location+ " "+now)
            request.session['gold'] += cavegold
            request.session['activities'].insert(0, {'string':string})
        elif request.POST['building'] == 'house':
            request.session['color'] = "earned"
            housegold = random.randint(2,5)
            location ="house"
            now = str(datetime.now())
            string = ("Earned " +str(housegold) + " golds from the " +location+ ""+now)
            request.session['gold'] += housegold
            request.session['activities'].insert(0, {'string':string})
        elif request.POST['building'] == 'casino':
            if request.session['gold'] <= 0:
                context={
                    msg: "Earn money to play",
                }
                # request.session['alert'] = "Go and earn money to pay in casino"
                return render(request,'ninjagold_app/index.html',context)
            else:
                casinogold = random.randint(-50,50)
                location ="casino"
                now = str(datetime.now())
                if casinogold <0 :
                    request.session['color']= "lost"
                    string = ("Lost " +str(casinogold) + " golds from the " +location+" "+now+ " Ouch!!!")
                else:
                    request.session['color']= "earned"
                    string = ("Earned " +str(casinogold) + " golds from the " +location+" "+now )
                request.session['gold'] += casinogold
                request.session['activities'].insert(0, {'string':string})

        return redirect('/')
    else:
            return redirect('/')
def clear(request):
                request.session['gold'] =0
                request.session['activities'] = []
                return redirect('/')
