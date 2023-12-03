from django.shortcuts import render
from .forms import contactForm

# Create your views here.

def home(request):
    return render(request, './first_app/home.html')
def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, './first_app/about.html', {'name': name, 'email': email })
    else:
        return render(request, './first_app/about.html')
def login(request):
    return render(request, './first_app/form.html')

def DjangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, './first_app/django_form.html',{'form':form})