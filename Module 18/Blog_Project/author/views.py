from django.shortcuts import render,redirect
from .import forms
# Create your views here.

# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             print(author_form.cleaned_data)
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'author.html',{'form':author_form})

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save()
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'registerform.html',{'form':register_form})