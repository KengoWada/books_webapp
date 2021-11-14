from django.db import models


class Book(models.Model):

    author = models.CharField(verbose_name='Author', max_length=100)
    title = models.CharField(verbose_name='Book Title', max_length=255)
    description = models.TextField(verbose_name='Book Description')
    release_date = models.DateField(verbose_name='Release Date')
    is_private = models.BooleanField(
        verbose_name='Is Book Private', default=False)

    class Meta:
        db_table = 'books'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
