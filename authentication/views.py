from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"form": form}
    return render(request, "register.html", context=context)


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"], password=form.cleaned_data["password"]
            )
            if user:
                django_login(request, user)
                return redirect("home")
            else:
                return redirect("register")

    context = {
        "form": form
    }

    return render(request, "login.html", context=context)

@login_required(login_url="login")
def logout(request):
    django_logout(request)

    return redirect("login")

@login_required(login_url="login")
def user_profile(request):

    return render(request, "user-profile.html")
