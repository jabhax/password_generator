from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    #return HttpResponse("<h1>EGGS!!!!!</h1>")
    return render(request, 'generator/home.html', {'password_lengths': [i for i in range(6, 15)]})

def about(request):
    about = ('This is a simple Password Generator. It can be customized by '
             'password length, uppercase, numbers, special characters, '
             'and swag.')
    return render(request, 'generator/about.html', {'about_text': about})

def password(request):
    base = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special = '!@#$%^&*()_+=-'
    characters = list(base)
    swag = False
    length = int(request.GET.get('length', 10))
    pw = ''

    if request.GET.get('uppercase'):
        characters.extend(base.upper())

    if request.GET.get('numbers'):
        characters.extend(numbers)

    if request.GET.get('special'):
        characters.extend(special)

    if request.GET.get('swag'):
        swag = True
         
    for i in range(length):
        pw += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': pw, 'swag': swag})
