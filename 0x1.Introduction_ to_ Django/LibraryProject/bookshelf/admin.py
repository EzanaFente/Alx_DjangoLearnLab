from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'published_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Fields to search by
    list_filter = ('published_year',)  # Add a filter for the published year

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)
