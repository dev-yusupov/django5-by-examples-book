from django.urls import path

from .views import user_login

app_name = "accounts"

urlpatterns = [
    path("login/", user_login, name="login"),
]
