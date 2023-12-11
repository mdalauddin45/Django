from django.urls import path,include
from .import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.userlogin, name='login'),
    path('logout/',views.userLogout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('passcharnge/',views.passcharnge, name='passcharnge'),
]
