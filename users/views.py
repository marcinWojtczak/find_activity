from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created ")
            return redirect('posts-view')
    else:
        form = UserRegisterForm
    
    return render(request, 'account/register.html', {"form": form})


