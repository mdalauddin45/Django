from django.urls import path,include
from .import views

urlpatterns = [
    path('profile/',views.add_profile, name='add_profile'),
]
