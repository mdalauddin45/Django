from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router = DefaultRouter()
router.register('', views.PatientViewset)

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]