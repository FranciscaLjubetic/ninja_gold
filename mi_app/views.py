from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import JsonResponse
from time import gmtime, strftime, localtime


def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")# Create your views here.

def func2(request):
    return HttpResponse("soy skynet :)")# Create your views here.

def saludaralvaro(request):
    return HttpResponse("hola alvaro :)")# Create your views here.

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect ("/")

def root(request):
    return redirect ("blogs/")

def show(request, number):
    return HttpResponse(f'placeholder para mostrar el blog numero: {number}')

def edit(request, number):
    return HttpResponse (f"placeholder para editar el blog {number}")

def destroy(request, number):
    return redirect("/blogs")

def json(request):
    return JsonResponse(
        {'nombe' : 'odio', 'edad' : 666, 'django': 'a morir',}
    )

def home(request, video):
    context = {
        'video': video,
        'mostrar': True,
        'imagenes': ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTslzdiofunV95P63ZJOa2Qe-DvOnwsjSRZvl9f02hRzw8zrfPe2qyzfXWHEAgRIfmqDlw&usqp=CAU', 
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjILEI-0o1_rB_K0QNwjMwYdmPDuToIGiVfM7O8AVs3gcen_4MU5uliMYSNjheq_CzqVg&usqp=CAU',
                    'https://pictures.abebooks.com/inventory/md/md30921047611.jpg',
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_wCKHySHrDfSZO8iVvoPNVinXjo0FRjOtMA&usqp=CAU'],
        'tmp': strftime('%b, %A, %Y  %H: %M', localtime())
        
    }
    return render(request, 'home.html', context)

def time(request):
    context = {
    "time": strftime('%b, %A, %Y  %H: %M', localtime())
    }
    return render(request, 'time.html', context)

def entrar(request, nombre):
    request.session['nombre'] = nombre
    
    return redirect('/home/<video>')

def salir(request):
    del request.session['nombre'] 
    return redirect('/home/<video>')


def login(request):
    #si llega un get, cargamos un formulario
    if request.method == 'GET':
        return render(request, 'formulario.html' )
    # si llega un post, logueamos al usuario(le mandammos un post a session con los datos del usuario)
    else:
        #print('nombre:', request.session['nombre']),
        #print('password:', request.session['password']),

        request.session['nombre'] = request.POST['nombre'],
        #request.session['password'] = request.POST['password'],
        return redirect('/time')
    #guardar los datos en session
    #redirigir a una pagina interna

