from django.shortcuts import render, HttpResponse, redirect
from .models import Users

def index(request):
    context={
        "cohort" : Users.objects.all()
    }
    return render(request,'index.html', context)

def go(request):
    if request.method == 'POST':
        name = request.POST ["name"]
        lname = request.POST ["last"]
        email = request.POST ["email"]
        age = request.POST ["age"]
    var = Users.objects.create(first_name = name, last_name = lname, email_address = email, age = age)
    var.save() 
    return redirect ("/")
