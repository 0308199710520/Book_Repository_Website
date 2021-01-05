from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):
    """View function for the home page of the site"""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()


    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
    }

    return render(request, "Index.html", context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = "my_book_list"
    queryset = Book.objects.filter(title__contains="war")
    template_name = "books"