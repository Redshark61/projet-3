from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/signup/1')
def home(request):
    context = {
        'user': request.user
    }
    return render(request, 'home:home', context)
