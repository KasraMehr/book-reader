from django.http import HttpResponse
from django.shortcuts import render

from library.models import Book


def index(request):
    book1 = Book.objects.all()
    response = ""
    return render(request, 'index.html', {'books': book1})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def books(request):
    book1 = Book.objects.all()
    return render(request, 'books.html', {'books': book1})


def library(request):
    # TODO: should return user's books...
    book1 = Book.objects.all()
    return render(request, 'books.html', {'books': book1})
