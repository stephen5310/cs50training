from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello It is Stephen here !</h1>")

def index_htm(request):
    return render(request, "cs50/index.html")


def greet_brian(request):
    return HttpResponse("Hello Brian !")

def greet_david(request):
    return HttpResponse("Hello David !")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()} !")

def greet_htm(request, name_in_url):
    return render(request, "cs50/greet.html", {
        "name_on_template": name_in_url.capitalize()
    })