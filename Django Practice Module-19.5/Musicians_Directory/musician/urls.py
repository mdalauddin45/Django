from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.MusicianAddView.as_view(), name='musician'),
]