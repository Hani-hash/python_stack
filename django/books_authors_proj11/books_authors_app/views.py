from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request):
    context = {
        'books': Book.objects.all()

    }
    return render(request, 'index.html', context)


def add_authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, "Authors.html", context)


def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')


def add_author(request):

    Author.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['Notes'])
    return redirect('/authors')


def book_display(request, id):
    context = {
        'bookss': Book.objects.get(id=id),
        'authors': Author.objects.all()
    }
    return render(request, "books_display.html", context)


def authors_info(request, id):
    context = {
        'authors': Author.objects.get(id=id),
        'books': Book.objects.all()
    }
    return render(request, "authors_info.html", context)


def addbookauthor(request, id):
    x = Author.objects.get(id=id)
    i = request.POST['id']
    x.books.add(Book.objects.get(id=i))
    return redirect('/authors/'+str(id))


def addauthorbook(request, id):
    x = Book.objects.get(id=id)
    i = request.POST['id']
    x.authors.add(Author.objects.get(id=i))
    return redirect('/books/'+str(id))
