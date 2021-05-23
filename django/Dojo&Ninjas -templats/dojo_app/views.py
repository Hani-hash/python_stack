from django.shortcuts import render, HttpResponse,redirect
from .models import *

def index(request):
    context = {
        'ninja':ninjas.objects.all(),
        'dojoos':dojos.objects.all()
    }
    return render(request,"index.html",context)

def add_dojo(request):
    dojos.objects.create(name = request.POST["name"],city = request.POST["city"],state = request.POST["state"])
    return redirect('/')


def insert_ninja(request):
    ninjas.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], dojo = dojos.objects.get(name= request.POST['ninjaa']))

    return redirect('/')