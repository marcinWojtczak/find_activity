from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name='logout-page')
]
