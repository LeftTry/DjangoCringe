from contextlib import redirect_stderr
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book, Author

def index(request):
    if request.method == 'GET':
        book_list = Book.objects.order_by('-pub_date')
        template = loader.get_template('index.html')
        context = {
            'book_list': book_list
        }
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        aname = request.POST.get('aname', '')
        surname = request.POST.get('surname', '')
        bday = request.POST.get('bday', '')
        if aname != None and surname != None and bday != None:
            au = Author.objects.get(name=aname, surname=surname)
            if au == None:
                author = Author.objects.create(name=aname, surname=surname, bday=bday)
        bname = request.POST.get('bname', '')
        if bname != None:
            text = request.POST.get('text', '')
            author = Author.objects.get(name=aname, surname=surname)
            book = Book.objects.create(name=bname, text=text, author=author)
        return redirect('/')

def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})
