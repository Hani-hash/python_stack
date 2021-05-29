from django.shortcuts import redirect, render, HttpResponse
import re
from django.contrib import messages
import bcrypt
from .models import *


def root(request):
    return render(request,('root.html'))

def register(request):
    
    Email_regex = EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors = {}
    if len(request.POST ['fname']) < 2:
        errors['fname'] = "This name is too short"
        
                
    if len(request.POST ['lname']) < 2:
        errors['lname'] = "This name is too short"
        

    if not Email_regex.match (request.POST['email']):
        errors['email'] = 'invalid email adress'

    if len(request.POST['passwd']) < 8:
        errors['passwd']='short password'
        

    if request.POST['passwd'] != request.POST['conpasswd']:
        errors['confirm']="Not Matching"
    for key,value in errors.items():
        if len(errors) > 0: 
            messages.error(request,value)
                

    else:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['passwd']
        confirm = request.POST['conpasswd']
        if password==confirm:
            hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name = first_name, last_name = last_name, email = email, passwd = hash)
            if 'name' not in request.session:
                request.session['name'] = first_name
            return redirect('/success')
        return redirect('/')



def success(request):
    return render(request,('success.html'))


def logout(request):
    del request.session['name']

    return redirect('/')


def login(request):
    user1 = User.objects.filter(email=request.POST['lemail'])
    if user1: #if len(user)>0
        if bcrypt.checkpw(request.POST['lpasswd'].encode(), user1[0].passwd.encode()):
           if 'name' not in request.session:
                request.session['name'] = user1[0].first_name
           return redirect('/success')
        return redirect('/')
    return redirect('/')
       
        

