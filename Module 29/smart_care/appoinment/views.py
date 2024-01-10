from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppoinmentSerializer

class AppoinmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppoinmentSerializer
    
    #custom queryset
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset