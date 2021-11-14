from django.urls import path

from .views import index, search, titles


urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search_books'),
    path('titles/', titles, name='titles'),
]
