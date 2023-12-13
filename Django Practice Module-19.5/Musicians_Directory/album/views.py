from django.shortcuts import render, redirect
from django.views import View
from . import models, forms
from .forms import AlbumForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView


@method_decorator(login_required, name='dispatch')
class AlbumAddView(View):
    template_name = 'album.html'
    form_class = AlbumForm
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Album created successfully")
            return redirect('home')
        else:
            messages.warning(request, "Creation failed")
            return render(request, self.template_name, {'form': form})
        
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        messages.success(self.request, "Album Updated successfully")
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    success_url = reverse_lazy('home')
    template_name = 'confirm_album_delete.html'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)