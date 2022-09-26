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

def book1(request):
    return render(request, '1.html')

def book2(request):
    return render(request, '2.html')

def book3(request):
    return render(request, '3.html')

def book4(request):
    return render(request, '4.html')

def book5(request):
    return render(request, '5.html')

def book6(request):
    return render(request, '5.html')

