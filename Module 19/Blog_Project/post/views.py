from typing import Any
from django.shortcuts import render,redirect
from .import forms
from .import models
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('profile')
    else:
        post_form = forms.PostForm()
    return render(request, 'post.html',{'form':post_form})

#Add post using class Based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            print(post_form.cleaned_data)
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home')
    return render(request, 'post.html',{'form':post_form})

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    
class DetailsPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object #post model er object akany store korlam
        comments = post.comments
        if self.request.method == "POST":
            comment_form = forms.CommentForm(data=self.request.post)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
        else:
            comment_form= forms.CommentForm()
            
        context['comments']= comments
        context['comment_form']= comment_form
        return context