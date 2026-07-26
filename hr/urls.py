from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.hr_dashboard, name="hr_dashboard"),
    path("candidate/<int:id>/", views.view_candidate, name="view_candidate"),
]