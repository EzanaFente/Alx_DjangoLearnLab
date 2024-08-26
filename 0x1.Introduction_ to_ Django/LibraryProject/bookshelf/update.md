from .models import Book

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)  # Output: Go Set a Watchman