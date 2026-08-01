from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Interview Scheduled", "Interview Scheduled"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]
    offer_letter = models.FileField(
    upload_to="offer_letters/",
    blank=True,
    null=True
)
    notification_read = models.BooleanField(default=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    applied_date = models.DateField()

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    interview_date = models.DateField(
    blank=True,
    null=True
    )

    interview_time = models.TimeField(
    blank=True,
    null=True
    )

    interview_link = models.URLField(
    blank=True,
    null=True
    )

    
    class Meta:
        ordering = ["-applied_date"]

    def __str__(self):
        return f"{self.company_name} - {self.job_role}"