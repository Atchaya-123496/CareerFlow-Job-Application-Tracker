from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import UserProfile
from .forms import UserProfileForm, RegisterForm
from django.contrib import messages


# ---------------- HOME ---------------- #


def home(request):
    return render(request, "accounts/home.html")


def learn_more(request):
    return render(request, "accounts/learn_more.html")


# ---------------- PROFILE ---------------- #
@login_required
def profile(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile saved successfully."
            )

            return redirect("profile")

    else:

        form = UserProfileForm(
            instance=profile
        )

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
            "profile": profile
        }
    )


# ---------------- REGISTER ---------------- #

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            role = form.cleaned_data["role"]

            UserProfile.objects.create(
                user=user,
                role=role
            )

            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )
# ---------------- LOGIN ---------------- #

def user_login(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(
                request,
                "accounts/login.html",
                {
                    "error": "Please enter username and password."
                }
            )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            profile, created = UserProfile.objects.get_or_create(
                user=user
            )

            if profile.role == "HR":
                return redirect("hr_dashboard")

            else:
                return redirect("dashboard")


        return render(
            request,
            "accounts/login.html",
            {
                "error": "Incorrect username or password."
            }
        )

    return render(
        request,
        "accounts/login.html"
    )

# ---------------- LOGOUT ---------------- #

def user_logout(request):
    logout(request)
    return redirect("home")