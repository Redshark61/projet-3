from django.shortcuts import render
from login_signup.forms import Connection1, LoginForm
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    request.session['medical'] = False
    return render(request, 'login_signup/index.html', {})


def signup(request, number):

    className = eval(f"Connection{number}")
    nextNumber = number + 1
    previousNumber = number - 1
    isMedical = request.session['medical']
    stepProgress = '12' if isMedical else '123456'
    context = {
        'next_id': nextNumber,
        'current_id': str(number),
        'prev_id': previousNumber,
        'is_medical': isMedical,
        'step_progress': stepProgress,
        'is_valid': True
    }
    if request.method == 'POST':
        form = className.__call__(request.POST)
        context['form'] = form
        if form.is_valid():
            if number == 1:
                user = User.objects.create_user(
                    form.cleaned_data['id_code'], form.cleaned_data['mail'], form.cleaned_data['password'])
                user.save()
                request.session['user_id'] = user.id
                return render(request, f'login_signup/signup/signup{nextNumber}.html', {})
        else:
            context['is_valid'] = False
            return render(request, f'login_signup/signup/signup{number}.html', context)
    else:
        form = className.__call__()
        context['form'] = form
        return render(request, f'login_signup/signup/{number}.html', context)


def signupMedical(request):
    request.session['medical'] = True
    return render(request, 'login_signup/signup/medical.html', {})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['id_code'])
            if user.check_password(form.cleaned_data['password']):
                request.session['user_id'] = user.id
                return render(request, 'login_signup/home/home.html', {'user_id': user.id})
            else:
                return render(request, 'login_signup/login.html', {'is_valid': False})
        else:
            return render(request, 'login_signup/login.html', {'is_valid': False})
    else:
        form = LoginForm()
        return render(request, 'login_signup/login.html', {'form': form})


def home(request):
    user_id = request.session['user_id']
    return render(request, 'login_signup/home/home.html', {'user_id': user_id})
