from . models import Post, Comment
from . forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView
)


def home(request):
    return render(request, 'activity/home.html')


class PostListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm

        context = {
            'form': form,
            'posts': posts
        }
        return render(request, 'activity/posts_list.html',context)


    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            form.save()
        context = {
            'form': form,
            'posts': posts
        }
        return render(request, 'activity/posts_list.html', context)


class PostDetailView(LoginRequiredMixin, View):
    
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm
        comment = Comment.objects.filter(post=post).order_by('-created_on')
        

        context = {
            'post': post,
            'form': form,
            'comments': comment
            
        }
        return render(request, 'activity/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        
        if form.is_valid():
            new_comment = form.save(commit=False )
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
        
        comment = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comment
        }
        return render(request, 'activity/post_detail.html', context)


# class PostDetailView(LoginRequiredMixin, DetailView):
#     model = Post
#     form_class =  
#     fields = '__all__'
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','localization', 'content']
    template_name = 'activity/post_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post=self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'activity/post_delete.html'
    success_url = reverse_lazy('posts-list')

    # def get_success_url(self):
    #     pk = self.kwargs['pk']
    #     return reverse_lazy('posts-list', kwargs={'pk': pk})

    def test_func(self):
        post=self.get_object()
        return self.request.user == post.author


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'activity/comment_update.html'
    

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment=self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'activity/comment_delete.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment=self.get_object()
        return self.request.user == comment.author


