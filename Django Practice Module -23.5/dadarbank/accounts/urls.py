
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,UserBankAccountUpdateView,charngepassword
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/', charngepassword, name='password_change'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]