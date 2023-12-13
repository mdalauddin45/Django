from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.registrationView.as_view(), name='register'),
    path('login/', views.UserLoginForm.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
