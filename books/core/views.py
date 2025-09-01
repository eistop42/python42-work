from django.http import HttpResponse
from django.shortcuts import render

from .models import Book, Category

def hello(request):
    """Главная страница"""

    return render(request, 'main.html')


def books(request):
    """Страница со списком книг"""

    books_list = Book.objects.all()
    category_list = Category.objects.all()

    category_id_from_url = request.GET.get('category')
    if category_id_from_url:
        print(category_id_from_url)
        books_list = books_list.filter(category__id=category_id_from_url)

    context = {'books_list': books_list, 'category_list':category_list }

    return render(request, 'books.html', context)