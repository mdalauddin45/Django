from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='homepage' ),
    path('about/',views.about, name='about_us' ),
    path('login/',views.login,name='submit_form' ),
    path('django_form/',views.passwordvalidition,name='django_form' ),
]
