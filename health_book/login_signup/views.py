from django.shortcuts import render

# Create your views here.


def index(request):
    request.session['medical'] = False
    print(request.session['medical'])
    return render(request, 'login_signup/index.html', {})


def signup(request, number):
    nextNumber = number + 1
    previousNumber = number - 1
    isMedical = request.session['medical']
    stepProgress = '12' if isMedical else '123456'
    context = {
        'next_id': nextNumber,
        'current_id': str(number),
        'prev_id': previousNumber,
        'is_medical': isMedical,
        'step_progress': stepProgress
    }
    return render(request, f'login_signup/signup/{number}.html', context)


def signupMedical(request):
    request.session['medical'] = True
    return render(request, 'login_signup/signup/medical.html', {})


def home(request):
    return render(request, 'login_signup/home/home.html', {})
