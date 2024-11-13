from django.db import models
"""testing docstring"""

class Author(models.Model):
    """
    this class represents the author with name, bio and age
    """
    name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        """
        returns the name of the author.
        """
        return self.name

class Book(models.Model):
    """
    this class is the book with title, description, publish date and the author
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField(Author, through='AuthorBook')
    fiction = models.BooleanField()

    def __str__(self):
        """
    returns title
    """
        return self.title

class AuthorBook(models.Model):
    """
    represents a relationship with author and book, indcluding contribution type and if author is primary author
    """
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contribution_date = models.DateField(auto_now_add=True)
    contribution_summary = models.TextField()