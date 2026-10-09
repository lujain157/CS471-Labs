
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get("name")

    if name:
        return HttpResponse("Hello from " + name + "!")

    return HttpResponse("Hello, world!")


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def bookmodule(request):
    return render(request, "bookmodule/bookmodule.html")


def template_variable(request):
    return render(
        request,
        "bookmodule/index.html",
        {"message": "Hello from Lujain!"}
    )


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    books = {
        123: {
            "id": 123,
            "title": "Continuous Delivery",
            "author": "Jez Humble and David Farley"
        }
    }

    book = books.get(bookId)

    if book is None:
        return HttpResponse("Book not found", status=404)

    return render(request, "bookmodule/show.html", {"book": book})
