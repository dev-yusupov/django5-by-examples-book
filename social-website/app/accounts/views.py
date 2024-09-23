from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import LoginForm

def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request=request,
                username=cd['username'],
                password=cd['password'],
            )

            if user is not None:
                if user.is_active:
                    login(request=request, user=user)
                    return HttpResponse("Authenticated successfully!")
                
                else:
                    return HttpResponse("Disabled user!")
            else:
                return HttpResponse('Invalid login')
            
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {
        "form": form,
    })