from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Fields to search by

# Register the Book model with custom admin options
admin.site.register(Book, BookAdmin)
