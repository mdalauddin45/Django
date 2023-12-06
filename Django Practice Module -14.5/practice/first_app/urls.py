from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('modelform/',views.modelform,name='modelform'),
]
