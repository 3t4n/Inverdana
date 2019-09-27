from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    return render(request, 'login.html')


def logintest():
    return '<h1>prueba</h1>'


@login_required
def home(request):
    return render(request, 'home.html')