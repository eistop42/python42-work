from django.http import HttpResponse
from django.shortcuts import render

from .models import Book

def hello(request):
    return HttpResponse('Hello world!')


def books(request):
    # books_list = [
    #     {'name': 'Идиот', 'author': 'Достоевский'},
    #     {'name': 'Война и мир', 'author': 'Толстой'}
    # ]
    books_list = Book.objects.all()
    context = {'books_list': books_list}

    return render(request, 'books.html', context)