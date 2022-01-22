from http.client import HTTPResponse
from re import template
from django.shortcuts import render

# Create your views here.


def index(request):
    request.session['medical'] = False
    print(request.session['medical'])
    return render(request, 'login_signup/index.html', {})


def signup(request, number):
    nextNumber = number + 1
    isMedical = request.session['medical']
    return render(request, f'login_signup/signup/{number}.html', {'id': nextNumber, 'isMedical': isMedical})


def signupMedical(request):
    request.session['medical'] = True
    return render(request, 'login_signup/signup/medical.html', {})


def home(request):
    return render(request, 'login_signup/home/home.html', {})
