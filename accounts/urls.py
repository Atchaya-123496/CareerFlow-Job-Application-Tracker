from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Learn More
    path("learn-more/", views.learn_more, name="learn_more"),

    # Profile
    path("profile/", views.profile, name="profile"),

    # Authentication
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.user_logout, name="logout"),
]