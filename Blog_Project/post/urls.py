from django.urls import path,include
from .import views

urlpatterns = [
    path('post/',views.add_post, name='add_post'),
]
