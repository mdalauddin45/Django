from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'profile.html')
def registration(request):
    return render(request, 'registration.html',{'type': 'registration'})
def userlogin(request):
    return render(request, 'registration.html',{'type': 'Login'})
def userlogout(request):
    return render(request, 'registration.html')
