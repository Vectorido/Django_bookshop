from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(null=True)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'Книга: {self.name} / Автор: {self.author} / Рейтинг: {self.rating} / Популярность: {"Yes" if self.is_best_selling == True else "No" }'

# Create your models here.
