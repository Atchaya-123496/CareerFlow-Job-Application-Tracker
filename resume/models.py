from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=100)

    email = models.EmailField(blank=True)

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    summary = models.TextField(blank=True)

    education = models.TextField(blank=True)

    skills = models.TextField(blank=True)

    projects = models.TextField(blank=True)

    experience = models.TextField(blank=True)

    linkedin = models.URLField(blank=True)

    github = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name