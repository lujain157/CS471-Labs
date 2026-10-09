
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('index2/<int:val1>/', views.index2, name='books.index2'),
    path('bookmodule/', views.bookmodule, name='books.bookmodule'),
    path('template/', views.template_variable, name='books.template'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
]
