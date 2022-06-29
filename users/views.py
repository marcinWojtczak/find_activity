from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm
from django.views import View
from activity.models import Post
from . models import UserProfile
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created ")
            return redirect('login-page')
    else:
        form = UserRegisterForm
    
    return render(request, 'users/register.html', {"form": form})


class ProfileView(View):

    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts
        }
        return render(request, 'users/profile.html', context)


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    template_name = 'users/profile_update.html'
    fields = ['name', 'email', 'birth_date', 'picture'] 

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile-page', kwargs={'pk': pk})

    def test_func(self):
        profile=self.get_object()
        return self.request.user == profile.user
    




