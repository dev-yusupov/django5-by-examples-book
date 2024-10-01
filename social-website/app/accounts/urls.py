from django.urls import path
from django.contrib.auth import views as auth_views

from .views import dashboard

# app_name = "accounts"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path("password-change/", auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password-change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password-change-done"),

    path("", dashboard, name="dashboard"),
]
