from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "bookmodule/index.html")


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def html5_links(request):
    return render(request, 'bookmodule/html5/links.html')

def html5_formatting(request):
    return render(request, 'bookmodule/html5/formatting.html')

def html5_listing(request):
    return render(request, 'bookmodule/html5/listing.html')

def html5_tables(request):
    return render(request, 'bookmodule/html5/tables.html')