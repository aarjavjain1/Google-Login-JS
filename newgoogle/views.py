from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def button(request):
    return render(request, 'base.html')
