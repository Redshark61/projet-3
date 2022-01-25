from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as loginUser
from django.shortcuts import redirect, render
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
                    username=request.POST['code_id'],
                    email=form.cleaned_data['mail'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
                user.save()
                loginUser(request, user)
                # return render(request, f'login_signup/signup/signup{nextNumber}.html', {})
                return redirect('home:home')
        else:
            context['is_valid'] = False
            return render(request, f'login_signup/signup/{number}.html', context)
    else:
        form = className.__call__()
        context['form'] = form
        return render(request, f'login_signup/signup/{number}.html', context)


def signupMedical(request):
    request.session['medical'] = True
    return redirect('login_signup:signup', 1)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['id_code'], password=form.cleaned_data['password'])
            if user is not None:
                loginUser(request, user)
                return redirect('home:home')
            else:
                return render(request, 'login_signup/login.html', {'is_valid': False})
        else:
            form = LoginForm()
            return render(request, 'login_signup/login.html', {'is_valid': False, 'form': form})
    else:
        form = LoginForm()
        return render(request, 'login_signup/login.html', {'form': form})
