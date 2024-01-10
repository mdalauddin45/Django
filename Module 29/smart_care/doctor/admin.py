from django.contrib import admin
from .models import Doctor,Specialization,Designation,AvailableTime,Review
# Register your models here.
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
admin.site.register(Specialization,SpecializationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
admin.site.register(Designation,DesignationAdmin)

admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)