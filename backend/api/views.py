import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Author, Book, AuthorBook

@csrf_exempt
def author_book(request):
    """
    View to handle CRUD operations for contribution
    """
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            contribution = AuthorBook.objects.create(
                author_id=data.get('author_id'),
                book_id=data.get('book_id'),
                is_primary_author=data.get('is_primary_author'),
                contribution_summary=data.get('contribution_summary')
            )
            return JsonResponse({'message': 'Contribution made!','date':contribution.date,'id': contribution.id}, status=201)

        elif request.method == 'GET':
            contributions = list(AuthorBook.objects.all().values())
            return JsonResponse({'cont': contributions, 'message': 'Contributions retrieved successfully!'}, status=200)

        elif request.method == 'PUT':
            data = json.loads(request.body)
            contribution = AuthorBook.objects.get(id=data.get('id'))
            contribution.book_id = data.get('book_id')
            contribution.author_id = data.get('author_id')
            contribution.is_primary_author = data.get('is_primary_author')
            contribution.contribution_summary = data.get('contribution_summary')
            contribution.save()
            return JsonResponse({'message': 'Contribution modified'}, status=200)

        elif request.method == 'DELETE':
            data = json.loads(request.body)
            contribution_id = data.get('id')
            AuthorBook.objects.get(id=contribution_id).delete()
            return JsonResponse({'message': 'Contribution deleted.'}, status=204)

        return JsonResponse({'message': 'Method Not Allowed.'}, status=405)

    except json.JSONDecodeError:
        return JsonResponse({'message': 'Request must be in JSON format'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def author_view(request):
    """
    View to handle CRUD operations for author model
    """
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            author = Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                age=data['age']
            )
return JsonResponse({'message': 'Author created successfully.', 'author': {'id': author.id}}, status=201)

        elif request.method == 'GET':
            authors = list(Author.objects.all().values())
            return JsonResponse({'authors': authors, 'message': 'Authors retrieved successfully.'}, status=200)

        elif request.method == 'PUT':
            data = json.loads(request.body)
            author = Author.objects.get(id=data['id'])
            author.name = data.get('name', author.name)
            author.bio = data.get('bio', author.bio)
            author.age = data.get('age', author.age)
            author.save()
            return JsonResponse({'message': 'Author modified.', 'cont': author}, status=200)

        elif request.method == 'DELETE':
            data = json.loads(request.body)
            author_id = data.get('id')
            Author.objects.get(id=author_id).delete()
            return JsonResponse({'message': 'Author deleted.'}, status=204)

        return JsonResponse({'message': 'Method Not Allowed.'}, status=405)

    except json.JSONDecodeError:
        return JsonResponse({'message': 'Request must be in JSON format'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def book_view(request):
    """
    View to handle CRUD operations for book model
    """
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            book = Book.objects.create(
                title=data['title'],
                description=data['description']
            )
            for contribution in data.get('author_contributions', []):
                author = Author.objects.get(name=contribution['author_name'])
                AuthorBook.objects.create(
                    book=book,
                    author=author,
                    is_primary_author=contribution['is_primary_author'],
                    contribution_date=contribution['contribution_date'],
                    contribution_summary=contribution['contribution_summary']
                )
            return JsonResponse({'message': 'Book created successfully.', 'id': book.id}, status=201)

        elif request.method == 'GET':
            books = Book.objects.all()
            books_data = []
            for book in books:
                author_contributions = []
                for contribution in book.authorbook_set.all():
                    author_contributions.append({
                        'id': contribution.id,
                        'author_name': contribution.author.name,
                        'is_primary_author': contribution.is_primary_author,
                        'contribution_date': contribution.contribution_date,
                        'contribution_summary': contribution.contribution_summary
                    })
                books_data.append({
                    'id': book.id,
                    'title': book.title,
                    'description': book.description,
                    'author_contributions': author_contributions
                })
            return JsonResponse({'books': books_data, 'message': 'Books retrieved successfully.'}, status=200)

        elif request.method == 'PUT':
            data = json.loads(request.body)
            book = Book.objects.get(id=data['id'])
            book.title = data.get('title', book.title)
            book.description = data.get('description', book.description)
            book.save()
            for contribution in data.get('author_contributions', []):
                author = Author.objects.get(id=contribution['author_id'])
                author_book = AuthorBook.objects.filter(book=book, author=author).first()
                if author_book:
                    author_book.is_primary_author = contribution.get('is_primary_author', author_book.is_primary_author)
                    author_book.contribution_summary = contribution.get('contribution_summary', author_book.contribution_summary)
                    author_book.save()
                else:
                    AuthorBook.objects.create(
                        book=book,
                        author=author,
                        is_primary_author=contribution['is_primary_author'],
                        contribution_date=contribution['contribution_date'],
                        contribution_summary=contribution['contribution_summary']
                    )
            return JsonResponse({'message': 'Book modified.', 'cont': book}, status=200)

        elif request.method == 'DELETE':
            data = json.loads(request.body)
            book_id = data.get('id')
            Book.objects.get(id=book_id).delete()
            return JsonResponse({'message': 'Book deleted.'}, status=204)

        return JsonResponse({'message': 'Method Not Allowed.'}, status=405)

    except json.JSONDecodeError:
        return JsonResponse({'message': 'Request must be in JSON format'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def test_api_view(request):
    return JsonResponse({'message': 'API is working!'}, status=200)