from .models import Book

# Verify the update
updated_book = Book.objects.get(published_date="Nineteen Eighty-Four")
print(updated_book.title)  # Output: Go Set a Watchman