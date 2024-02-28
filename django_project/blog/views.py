from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    #there are couple of ways to load a template
    #one way would be load it and render and then pass it to httpresponse (needs more steps)
    #django provides a shortcut that provide a way to do all of this in one just piece of code
    context={
       
        'posts':Post.objects.all()
    }
    return render(request,"blog/home.html",context,{'title':'Homepage'})
class PostListViw(ListView):
    #we will create a variable named model which will tell our ListView what model to query
    #in order to create the List
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']#date_posted will order our post in form of oldest to newest however minus sign will make it newset to oldest
    paginate_by=3
class UserPostListViw(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=3
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    
    model=Post
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
       
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
       
        return False
def about(request):
    return render(request,'blog/about.html')