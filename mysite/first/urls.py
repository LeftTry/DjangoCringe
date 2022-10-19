from django.urls import path, re_path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.view_book, name='view_book'),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete_book, name='delete_book'),
    re_path(r'^delete/author/(?P<pk>[0-9]+)/$', views.delete_author, name='delete_author')
]
