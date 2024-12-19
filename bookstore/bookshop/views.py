# bookshop/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def books(request):
    return render(request, 'books.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
