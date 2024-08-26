from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'publication_year')  # Include publication_year in list_display
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)  # Filter by publication_year

admin.site.register(Book, BookAdmin)
