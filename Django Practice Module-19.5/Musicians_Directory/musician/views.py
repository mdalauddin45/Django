from django.shortcuts import render,redirect
from django.views import View
from .import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required, name='dispatch')
class MusicianAddView(View):
    template_name = 'musician.html'
    form_class = forms.MusicianForm
    success_url = reverse_lazy('home')
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Musician created successfully")
            return redirect('home')
        else:
            messages.warning(request, "Creation failed")
            return render(request, self.template_name, {'form': form})