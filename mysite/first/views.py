from contextlib import redirect_stderr
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book, Author
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, FileResponse
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'GET':
        book_list = Book.objects.order_by('-name')
        template = loader.get_template('index.html')
        context = {
            'book_list': book_list
        }
        return HttpResponse(template.render(context, request))
    if request.method == 'POST':
        aname = request.POST.get('aname', '')
        surname = request.POST.get('surname', '')
        if aname != None and surname != None:
            try:
                au = Author.objects.get(name=aname, surname=surname)
            except:
                au = None
                pass
            if au == None:
                author = Author.objects.create(name=aname, surname=surname)
        bname = request.POST.get('bname', '')
        if bname != None:
            text = request.POST.get('text', '')
            author = Author.objects.get(name=aname, surname=surname)
            book = Book.objects.create(name=bname, text=text, author=author)
            print(bname)
            print(book.name)
            print(book.id)
        return redirect('/')

def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  

    if request.method == 'POST':         
        book.delete()                     
        return redirect('/')

    return render(request, 'index.html', {'book': book})

def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)  
    if request.method == 'POST':         
        author.delete()
        book_list = Book.objects.order_by('-name')
        for i in book_list:
            if i.author == author:
                i.delete()
        return redirect('/')

    return render(request, 'index.html', {'author': author})

def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/index')
        return render(request, 'logpage.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return redirect('/')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            return redirect('/')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/')
