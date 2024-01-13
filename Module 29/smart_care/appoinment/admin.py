from django.contrib import admin
from .models import Appointment
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['patient_name','doctor_name', "appointment_types","appointment_status","symptom","time","cancel"]
    
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def doctor_name(self,obj):
        return obj.doctor.user.last_name
    
    def save_model(self,rquest,obj,form,change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject = "Your Online Appointment Is Running"
            email_body = render_to_string('admin_email.html',{'user': obj.patient.user, 'doctor': obj.doctor})
            send_email = EmailMultiAlternatives(email_subject, '',to=[obj.patient.user.email])
            send_email.attach_alternative(email_body, "text/html")
            send_email.send()
    
admin.site.register(Appointment,AppointmentAdmin)