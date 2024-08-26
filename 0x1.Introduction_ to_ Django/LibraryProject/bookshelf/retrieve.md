from .models import Book

# Retrieve the created Book
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author)  # Output: To Kill a Mockingbird Harper Lee