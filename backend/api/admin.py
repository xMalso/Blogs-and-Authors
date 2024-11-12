from django.contrib import admin
from .models import Author, Book, AuthorBook  # Import the Contribution model

# Register each model to make it accessible in the admin interface
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(AuthorBook)