from django.shortcuts import render, render

def home_view(request):
    return render(request, 'home.html', {})

# Create your views here.
