

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def auth(user):
    if user is None or user.id is None:
        return redirect('login')


def index(request):
    return render(request, 'restaurant/index.html')
