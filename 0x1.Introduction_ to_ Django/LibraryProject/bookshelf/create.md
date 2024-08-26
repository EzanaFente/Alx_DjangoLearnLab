from .models import Book

# Create a Book instance
book = Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee', published_year=1960, genre='Fiction')
