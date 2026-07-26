from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.resume_builder,
        name="resume"
    ),
    path("preview/", views.resume_preview, name="resume_preview"),
    path(
    "download/",
    views.download_resume_pdf,
    name="download_resume_pdf"
),
]