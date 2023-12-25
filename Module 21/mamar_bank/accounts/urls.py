from django.urls import path
from .views import UserRegistrationView, UserLogoutView, UserLoinView,UserBankAccountUpdateView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoinView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]
