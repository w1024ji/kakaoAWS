# mainPage/views.py

from django.shortcuts import render
from django.http import HttpResponse

def mainPage(request):
    return render(request, 'mainPage/mainPage.html')



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
