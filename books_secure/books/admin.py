from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'release_date', 'is_private']
    list_filter = ['release_date', 'is_private']
    search_fields = ['author', 'title']


admin.site.register(Book, BookAdmin)
