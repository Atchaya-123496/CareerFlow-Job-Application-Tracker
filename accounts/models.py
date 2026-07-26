from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    education = models.CharField(
        max_length=200,
        blank=True
    )

    skills = models.TextField(
        blank=True,
        help_text="Example: Python, SQL, Excel, Power BI"
    )

    linkedin = models.URLField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    ROLE_CHOICES = [
        ("Candidate", "Candidate"),
        ("HR", "HR"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Candidate"
    )

    company = models.CharField(
    max_length=100,
    blank=True,
    null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username