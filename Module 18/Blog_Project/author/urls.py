from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.add_author, name='add_author'),
]
