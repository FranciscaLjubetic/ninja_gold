from django.shortcuts import render, redirect
from django.views import View
import random


# Create your views here.
def index(request):
    if 'gld' not in request.session:
        request.session['gld'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    
        
    return render(request, 'index.html')

def processmoney(request, name):

    if name == 'FARM':
        min = 10
        max = 20
            
    elif name == 'CAVE':
        min = 5
        max = 10

    elif name == 'HOUSE':
        min = 2
        max = 5
            
    else:
        min = -50
        max = 50
        
    gold = random.randint(min, max)

    
    request.session['gld'] += gold
    request.session['activities'].append({
        'text': f'You have {"won" if gold>=0 else "lost"} {gold} golds',
        'golds': gold,
    })
    return redirect('/ninjagold')
    

def reset(request):
    request.session['gld'] = 0
    return redirect("/ninjagold")

#def config(request, name):
    #default
    #if 'intents' not in request.POST:
        #request.POST['intents'] = 3
    #if 'amount' not in request.POST:
        #request.POST['amount'] = 20    

    #if name == 'SUBMIT':
            #if len(request.session['activities']) > request.POST['intents'] & request.session['gld'] <= request.POST['amount']:
                #request.session['activities'].append({
                #'text': f'you have exceeded the number of attempts. You have lost :(',
                #})
                #request.session['gld'] = 0

            #elif len(request.session['activities']) <= request.POST['intents'] & request.session['gld'] > request.POST['amount']:
                #request.session['activities'].append({
                #'text': f'you have win',
                #})
               # request.session['gld'] = 0
    #return redirect("/ninjagold")
    #return render(request, 'index.html')


    

    