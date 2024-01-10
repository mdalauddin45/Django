from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppoinmentSerializer

class AppoinmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppoinmentSerializer