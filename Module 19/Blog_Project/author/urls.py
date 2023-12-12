from django.urls import path,include
from .import views

urlpatterns = [
    path('register/',views.register, name='register'),
    # path('login/',views.userlogin, name='login'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/',views.userLogout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/edit/',views.edit_profile, name='edit_profile'),
    path('profile/edit/passcharnge/',views.passcharnge, name='passcharnge'),
]
