from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import UserSignupForm
from .models import tbBooking

# Create your views here.


def auth(user):
    """
    If user is not authenticated, redirect to login.
    """
    if user is None or user.id is None:
        return redirect('login')


def index(request):
    """
    Renders home page.
    """
    return render(request, 'restaurant/index.html')


def loginuser(request):
    """
    Enables user to login with form, checks validation.
    """
    if request.method == 'GET':
        return render(request, 'restaurant/loginuser.html',
                      {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'restaurant/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error': 'Username and password do not match.'})
        else:
            login(request, user)
            return redirect('index')


def logoutuser(request):
    """
    Enables user to logout.
    """
    logout(request)
    return redirect('index')


def register(request):
    """
    Enables user to sign-up with form validation and checks if username taken.
    """
    if request.method == 'GET':
        return render(request, 'restaurant/register.html',
                      {'form': UserSignupForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request,
                              'restaurant/register.html',
                              {'form': UserSignupForm,
                               'error': 'Username taken, choose another one.'})
        else:
            return render(request, 'restaurant/register.html',
                          {'form': UserSignupForm,
                           'error': 'Passwords do not match.'})


def booking(request):
    """
    Enables user make reservation with date, time and number of guests.
    Checks if django can handle if a user is authenticated
    to avoid checking all the time.
    """
    user = request.user
    auth(user)
    if request.method == 'GET':
        return render(request, 'restaurant/booking.html',
                      {'form': BookingForm()})

    elif request.method == 'POST':
        try:
            guests_str = request.POST.get('guests')
            guests = None
            if guests_str.isnumeric():
                guests = int(guests_str)
            if guests is None or guests < 1:
                return render(request,
                              'restaurant/booking.html',
                              {'form': BookingForm(),
                               'error': 'input guests number.'})

            date_str = request.POST.get('date')
            date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
            if date is None:
                return render(request,
                              'restaurant/booking.html',
                              {'form': BookingForm(),
                               'error': 'input date and time'})

            newBooking = tbBooking.objects.create(
                user=user,
                date=date.isoformat(),
                guests=guests,
                status=1)
            newBooking.save()

            return redirect('#')
        except ValueError:
            return render(request, 'restaurant/booking.html',
                          {'form': BookingForm(), 'error': 'bad data passed in'})
    else:
        return render(request, 'restaurant/booking.html')