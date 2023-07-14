from django.urls import path
from mrwrestaurant import views as mrwViews

urlpatterns = [
    path('', mrwViews.index, name='index'),
    path('login', mrwViews.loginuser, name='loginuser'),
    path('logout', mrwViews.logoutuser, name='logoutuser'),
]
