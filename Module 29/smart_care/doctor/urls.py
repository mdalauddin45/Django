from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router = DefaultRouter()
router.register('list',views.DoctorViewset)
router.register('specialization',views.SpecializationViewset, basename='SpecializationViewset')
router.register('designation',views.DesignationViewset, basename='DesignationViewset')
router.register('availabletime',views.AvailableTimeViewset, basename='AvailableTimeViewset')
router.register('review',views.ReviewViewset, basename='ReviewViewset')

urlpatterns = [
    path('', include(router.urls)),
]