from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='название категории')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300, verbose_name='название книги')
    author = models.CharField(max_length=255, verbose_name='автор')
    price = models.IntegerField(verbose_name='цена')
    category = models.ForeignKey(Category, verbose_name='категория', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.name


