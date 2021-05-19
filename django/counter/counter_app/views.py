from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if not('number' in request.session ):
        request.session["number"]=0
    if not('num' in request.session ):
        request.session["num"]=0
    request.session["number"]+=1
    request.session["num"]+=1
    return render(request,"index.html")

def destroy(request):
    request.session["number"]=0
    return redirect("/")

def addtwo(request):
    request.session["number"]+=1
    return redirect("/")

def increment(request,):

    request.session["number"]+=int(request.POST["number1"])-1
    return redirect("/")