from django.shortcuts import render

def home(request):
    return render(request, "glossary/home.html")