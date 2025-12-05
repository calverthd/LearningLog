from django.shortcuts import render

def home(request):
    return render(request, 'logs/home.html')

from django.shortcuts import render

def about(request):
    return render(request, 'logs/about.html')

from django.shortcuts import render

def contact(request):
    return render(request, 'logs/contact.html')

