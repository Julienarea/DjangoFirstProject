from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home",
        "content": "Главная страница",
        "list": ["first", "second"],
        "dict": {"key1": "value1", "key2": "value2"},
        "is_authenticated": False,
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About Page")
