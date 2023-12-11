from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse_lazy

from .forms import RegisterForm, LoginForm
from account.tokens import account_activation_token
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            subject = f'Activate Your {current_site.domain} Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect("login")
    context = {"form": form}
    return render(request, "register.html", context=context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        # user.profile.email_confirmed = True
        user.save()
        return redirect('login')
    else:
        return render(request, 'account_activation_invalid.html')


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
                return redirect("core:home")
            else:
                return redirect("account:register")

    context = {
        "form": form
    }

    return render(request, "login.html", context=context)

@login_required(login_url=reverse_lazy("account:login"))
def logout(request):
    django_logout(request)

    return redirect("account:login")

@login_required(login_url=reverse_lazy("account:login"))
def user_profile(request):

    return render(request, "user-profile.html")
