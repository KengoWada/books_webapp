from django.shortcuts import render

from .models import Book


def index(request):
    books = Book.objects.filter(is_private=False).order_by('release_date')
    return render(request, 'books/index.html', context={'books': books})


def search(request):
    q = request.GET.get('q', '')
    query = f"SELECT * FROM books WHERE title LIKE '%{q}%' AND is_private='f' ORDER BY release_date"
    books = Book.objects.raw(query)
    return render(request, 'books/index.html', context={'books': books, 'search_term': q})


def titles(request):
    books = Book.objects.all().order_by('release_date')

    titles = [None]*5
    for i in range(0, len(books)):
        titles[i] = books[i].title

    return render(request, template_name='books/titles.html', context={'titles': titles})
