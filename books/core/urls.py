from django.urls import path

from .views import hello, books

urlpatterns = [
    path('', hello),
    path('books', books)
]