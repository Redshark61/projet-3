from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'login_signup/index.html', {})


def signup(request, number):
    return render(request, f'login_signup/signup/{number}.html', {})


def signupMedical(request):
    return render(request, 'login_signup/signup/medical.html', {})


def home(request):
    return render(request, 'login_signup/home/home.html', {})
