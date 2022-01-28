from django.contrib.auth import authenticate, login as loginUser
from django.shortcuts import redirect, render
from login_signup.forms import *
from django.contrib.auth.models import User
from login_signup.models import User as ModelUser
# Create your views here.


def index(request):
    request.session['medical'] = False
    if request.method == 'POST':
        person, direction = request.POST.get('button').split("&")

        if person == 'personal':
            request.session['medical'] = False
            if direction == 'login':
                return redirect('login')
            if direction == 'signup':
                return redirect('login_signup:signup', 1)

        elif person == 'medical':
            request.session['medical'] = True
            if direction == 'login':
                return redirect('login')
            if direction == 'signup':
                return redirect('login_signup:signup', 1)
    return render(request, 'login_signup/index.html', {})


def signup(request, number):

    className = eval(f"Connection{number}")
    nextNumber = number + 1
    previousNumber = number - 1
    print(type(number), number)
    isMedical = request.session.get('medical')
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
                print("in signup 1")
                user = User.objects.create_user(
                    username=request.POST['code_id'],
                    email=form.cleaned_data['mail'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
                user.save()
                loginUser(request, user)
                return redirect('login_signup:signup', nextNumber)
            elif number == 2:
                signup = form.save(commit=False)
                signup.user = request.user
                signup.save()
                print("in signup 2")
                return redirect('login_signup:signup', nextNumber)
            elif number == 3:
                print("in signup 3")
                print(request.POST)
                location = form.save(commit=False)
                location.postal_code = request.POST['postal_code']
                location.save()
                currentUserData = ModelUser.objects.get(user=request.user)
                currentUserData.address_id = location
                currentUserData.save()
                return redirect('home:home')
        else:
            print("invalid form")
            context['is_valid'] = False
            return render(request, f'login_signup/signup/{number}.html', context)
    else:
        print("in signup else")
        form = className.__call__()
        context['form'] = form
        return render(request, f'login_signup/signup/{number}.html', context)


def signupMedical(request):
    request.session['isMedical'] = True
    return redirect('login_signup:signup', 1)


def login(request):

    def deleteField(request):
        if request.session.get('medical'):
            del form.fields['id_code']
            return 'rpps_code'
        else:
            del form.fields['rpps_code']
            return 'id_code'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = deleteField(request)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data[username], password=form.cleaned_data['password'])
            if user is not None:
                loginUser(request, user)
                return redirect('home:home')
            else:
                return render(request, 'login_signup:login', {'form': form, 'is_valid': False})
        else:
            form = LoginForm()
            deleteField(request)
            return render(request, 'login_signup:login', {'is_valid': False, 'form': form})
    else:
        form = LoginForm()
        deleteField(request)

        return render(request, 'login_signup:login', {'form': form, 'is_valid': True})
