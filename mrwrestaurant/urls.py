from django.urls import path
from mrwrestaurant import views as mrwViews

urlpatterns = [
    path('', mrwViews.index, name='index'),
    path('login', mrwViews.loginuser, name='loginuser'),
    path('logout', mrwViews.logoutuser, name='logoutuser'),
    path('resgister', mrwViews.register, name='register'),
    path('booking', mrwViews.booking, name='booking'),
    path('booklist', mrwViews.booklist, name='booklist'),
    path('contact', mrwViews.contact, name='contact'),
    path('userlist', mrwViews.userlist, name='userlist'),
    path('edituser/<int:user_id>/', mrwViews.edituser, name='edituser'),
    path('menu', mrwViews.menu, name='menu'),
]

handler404 = 'mrwrestaurant.views.handler_404'
