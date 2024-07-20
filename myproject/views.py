# from django.http import HttpResponse

# def homepage(request):
#     return HttpResponse("<h1>Home Page</h1>")

# def about(request):
#     return HttpResponse("<h1>About Page</h1>")

from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")