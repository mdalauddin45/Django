from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home),
    path('courses/', views.courses),
    path('about/', views.about),
]
