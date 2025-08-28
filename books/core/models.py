from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=300, verbose_name='название книги')
    author = models.CharField(max_length=255, verbose_name='автор')
    price = models.IntegerField(verbose_name='цена')

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.name
