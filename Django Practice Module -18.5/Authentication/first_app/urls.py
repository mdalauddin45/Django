from django.urls import path
from .import views
urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('register/',views.registration,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('charngepassword/',views.charngepassword,name='charngepassword'),
]
