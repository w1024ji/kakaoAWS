# mainPage/views.py

from django.shortcuts import render
from django.http import HttpResponse

def mainPage(request):

    print("main page 잘 작동한다!")
    return render(request, 'mainPage/mainPage.html')


