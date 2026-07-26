from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from tracker.models import JobApplication
from accounts.models import UserProfile


@login_required
def hr_dashboard(request):

    profile = UserProfile.objects.get(user=request.user)

    jobs = JobApplication.objects.select_related("user").filter(
            company_name=profile.company
        )


    context = {
        "jobs": jobs,
        "total": jobs.count(),
        "applied": jobs.filter(status="Applied").count(),
        "interview": jobs.filter(status="Interview Scheduled").count(),
        "selected": jobs.filter(status="Selected").count(),
        "rejected": jobs.filter(status="Rejected").count(),
    }

    return render(
        request,
        "hr/dashboard.html",
        context
    )


@login_required
def view_candidate(request, id):

    job = get_object_or_404(JobApplication, id=id)

    profile, created = UserProfile.objects.get_or_create(
        user=job.user
    )

    if request.method == "POST":

        # Status Update Form
        if "status" in request.POST:

            job.status = request.POST.get("status")
            job.interview_date = request.POST.get("interview_date") or None
            job.interview_time = request.POST.get("interview_time") or None
            job.interview_link = request.POST.get("interview_link")

            job.save()

            messages.success(
                request,
                "Application status updated successfully."
            )

        # Offer Letter Upload Form
        elif "offer_letter" in request.FILES:

            job.offer_letter = request.FILES["offer_letter"]
            job.save()

            messages.success(
                request,
                "Offer Letter uploaded successfully."
            )

        return redirect("view_candidate", id=job.id)

    return render(
        request,
        "tracker/view_candidate.html",
        {
            "job": job,
            "profile": profile,
        }
    )