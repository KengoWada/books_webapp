from django.shortcuts import render

from .models import Book


def index(request):
    books = Book.objects.filter(is_private=False).order_by('release_date')
    return render(request, 'books/index.html', context={'books': books})


def search(request):
    q = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=q).order_by('release_date')
    return render(request, 'books/index.html', context={'books': books, 'search_term': q})


def titles(request):
    books = Book.objects.filter(is_private=False).order_by('release_date')

    titles = []
    for book in books:
        titles.append(book.title)

    return render(request, template_name='books/titles.html', context={'titles': titles})
