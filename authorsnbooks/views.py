from django.shortcuts import render, redirect
from authorsnbooks.models import Books, Authors

def index(request):
    context = {
        'all_authors' : Authors.objects.all(),
        'all_books' : Books.objects.all()
    }
    return render(request, 'index.html', context)


def add_book(request):
    Books.objects.create(title = request.POST['book_title'], 
                        desc = request.POST['book_description'])
    return redirect('/books')

def add_author(request):
    Authors.objects.create(first_name = request.POST['first_name'], 
                        last_name = request.POST['last_name'],
                        notes = request.POST['author_notes'] )
    return redirect('/authors')

def delete_book(request, book_id):
    Books.objects.filter(id=int(book_id)).delete()
    return redirect('/books')

def delete_author(request, author_id):
    Authors.objects.filter(id=int(author_id)).delete()
    return redirect('/authors')

def books_page(request):
    context = {
        'all_books' : Books.objects.all()
    }
    return render(request, 'books_page.html', context)

def authors_page(request):
    context = {
        'all_authors' : Authors.objects.all(),
    }
    return render(request, 'authors_page.html', context)

def view_book(request, book_id):
    book = Books.objects.get(id=int(book_id))
    authors_id = [author.id for author in book.authors.all()]
    authors = Authors.objects.all()
    authors = [author for author in authors if author.id not in authors_id]
    
    context = {
        'book_title' : book.title,
        'book_id' : int(book.id),
        'book_description' : book.desc,
        'authors' : book.authors.all(),
        'all_authors' : authors
    }
    return render(request, 'view_books.html', context)

def view_author(request, author_id):
    author = Authors.objects.get(id=int(author_id))
    books_id = [books.id for books in author.books.all()]
    books = Books.objects.all()
    books = [book for book in books if book.id not in books_id]

    context = {
        'first_name' : author.first_name,
        'last_name' : author.last_name,
        'author_id' : int(author.id),
        'author_notes' : author.notes,
        'books' : author.books.all(),
        'all_books' : books
    }
    return render(request, 'view_authors.html', context)

def delete(request, author_id, book_id):
    author = Authors.objects.get(id=int(author_id))
    book = Books.objects.get(id=int(book_id))

    author.books.remove(book)

    return redirect(request.META.get('HTTP_REFERER'))

def add(request):
    author = Authors.objects.get(id=int(request.POST['author_id']))
    book = Books.objects.get(id=int(request.POST['book_id']))

    author.books.add(book)

    return redirect(request.META.get('HTTP_REFERER'))
