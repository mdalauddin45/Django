from django.shortcuts import render,redirect
from .import forms

# Create your views here.
# def add_category(request):
#     if request.method == 'POST':
#         category_form = forms.CategoryForm(request.POST)
#         if category_form.is_valid():
#             print(category_form.cleaned_data)
#             category_form.save()
#             return redirect('add_category')
#     else:
#         category_form = forms.CategoryForm()
#     return render(request, 'category.html',{'form':category_form})