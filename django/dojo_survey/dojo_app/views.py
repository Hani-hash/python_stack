from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def root(request):
    return render(request,'index.html')

def index(request):
    print("Got Post Info....................")
    name = request.POST['name']
    request.session['name'] = request.POST['name']
    select = request.POST['select']
    lang = request.POST['lang']
    
    comment = request.POST['comment']
    context = {

    	"name" : name,
    	"select" : select,
        "lang" : lang,
        
        "comment": comment,

    }
    return render(request,"show.html", context)


def trial(request):
    print(request.session['name'])
    return HttpResponse("now i can have a seet nigght after this struggle")

    