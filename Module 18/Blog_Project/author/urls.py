from django.urls import path,include
from .import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.userlogin, name='login'),
    path('logout/',views.userLogout, name='logout'),
]
