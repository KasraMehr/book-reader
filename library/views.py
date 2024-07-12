from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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
    book_list = Book.objects.defer('pdf_file').all()
    return render(request, 'books.html', {'books': book_list})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})