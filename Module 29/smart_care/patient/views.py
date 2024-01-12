from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer,RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# Create your views here.

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print("Registration", user)
            token = default_token_generator.make_token(user)
            print("token", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid", uid)
            confirm_link = f'http://127.0.0.1:8000/patient/active/{uid}/{token}'
            print("confirm_link", confirm_link)
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html',{'confirm_link': confirm_link})
            send_email = EmailMultiAlternatives(email_subject, '',to=[user.email])
            send_email.attach_alternative(email_body, "text/html")
            send_email.send()
            return Response("Check your email address for confirmation")
        return Response(serializer.errors)
