from django.shortcuts import render
from . models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    ListView, 
)

def home(request):
    return render(request, 'activity/home.html')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'activity/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-created_on']
