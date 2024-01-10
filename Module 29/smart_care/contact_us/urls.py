from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router = DefaultRouter()
router.register('contact_us', views.ContactUsViewset, basename='contact_us')

urlpatterns = [
    path('', include(router.urls)),
]