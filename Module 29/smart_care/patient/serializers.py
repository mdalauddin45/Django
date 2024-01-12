from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name','email', 'password','confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data.get('email')
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'Error':'password Does not match'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Error':'Email already exists'})
        
        account = User(username=username, email=email, last_name=last_name, first_name=first_name)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account