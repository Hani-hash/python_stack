from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if not('number' in request.session ):
        request.session["number"]=1
    if not('num' in request.session ):
        request.session["num"]=1
    request.session["number"]+=1
    request.session["num"]+=1
    return render(request,"index.html")

def destroy(request):
    request.session["number"]=0
    
    return render(request,"index.html")

def addtwo(request):
    request.session["number"]+=1
    return render(request,"index.html")

def increment(request,):
    request.session["number"]+=int(request.POST["number1"])-1
    return render(request,"index.html")