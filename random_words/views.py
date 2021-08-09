from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if request.session['counter'] <= 9:
        request.session['counter'] += 1

    
    
    


    context = {
        'randomword': get_random_string(length=14),
    }
    return render(request, 'random.html', context)


def reset(request):
    request.session['counter'] = 0
    return redirect("/random_words")











