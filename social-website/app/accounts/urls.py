from django.urls import path
from django.contrib.auth import views as auth_views

from .views import dashboard

# app_name = "accounts"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path("password-change/", auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password-change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name="password_change_done"),

    # Password reset urls
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    path("password-reset-done", auth_views.PasswordChangeDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uid64>/token/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("", dashboard, name="dashboard"),
]
