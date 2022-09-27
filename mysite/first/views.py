from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Book, Author

def index(request):
    book_list = Book.objects.order_by('-pub_date')
    template = loader.get_template('index.html')
    context = {
        'book_list': book_list
    }
    return HttpResponse(template.render(context, request))

def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})
