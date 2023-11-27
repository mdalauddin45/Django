
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home),
    path('blog/',views.earthlyblog)
]