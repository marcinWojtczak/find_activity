from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile-page'),
    path('profile/update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout-page')
]
