from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books_page, name="books_page"),
    path('authors', views.authors_page, name="authors_page"),
    path('delete_book/<book_id>', views.delete_book, name="delete_book"),
    path('delete_author/<author_id>', views.delete_author, name="delete_author"),
    path('delete/<author_id>/<book_id>', views.delete, name="delete"),
    path('add', views.add, name="add"),
    path('add_book', views.add_book, name="add_book"),
    path('add_author', views.add_author, name="add_author"),
    path('books/<book_id>', views.view_book, name="view_book"),
    path('authors/<author_id>', views.view_author, name="view_author")
]

