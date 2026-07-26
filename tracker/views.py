from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import JobApplication
from accounts.models import UserProfile
from .forms import JobApplicationForm



# ---------------- DASHBOARD ---------------- #

@login_required
def dashboard(request):

    search = request.GET.get("search", "")

    jobs = JobApplication.objects.filter(user=request.user)

    if search:
        jobs = jobs.filter(
            company_name__icontains=search
        ) | jobs.filter(
            job_role__icontains=search
        )

    jobs = jobs.order_by("-applied_date")

    context = {
        "jobs": jobs,
        "search": search,

        "total": jobs.count(),
        "applied": jobs.filter(status="Applied").count(),
        "interview": jobs.filter(status="Interview Scheduled").count(),
        "selected": jobs.filter(status="Selected").count(),
        "rejected": jobs.filter(status="Rejected").count(),
    }

    return render(
        request,
        "tracker/dashboard.html",
        context
    )


# ---------------- ADD JOB ---------------- #

# ---------------- ADD JOB ---------------- #

@login_required
def add_job(request):

    if request.method == "POST":

        form = JobApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            job = form.save(commit=False)
            job.user = request.user
            job.save()

            messages.success(
                request,
                "Job added successfully."
            )

            return redirect("dashboard")

    else:
        form = JobApplicationForm()

    return render(
        request,
        "tracker/add_job.html",
        {
            "form": form,
            "title": "Add Job"
        }
    )
# ---------------- EDIT JOB ---------------- #

@login_required
def edit_job(request, id):

    job = get_object_or_404(
        JobApplication,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = JobApplicationForm(
            request.POST,
            request.FILES,
            instance=job
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Job updated successfully."
            )

            return redirect("dashboard")

    else:

        form = JobApplicationForm(instance=job)

    return render(
        request,
        "tracker/add_job.html",
        {
            "form": form,
            "title": "Edit Job"
        }
    )


# ---------------- DELETE JOB ---------------- #

@login_required
def delete_job(request, id):

    job = get_object_or_404(
        JobApplication,
        id=id,
        user=request.user
    )

    job.delete()

    messages.success(
        request,
        "Job deleted successfully."
    )

    return redirect("dashboard")


# ---------------- NOTIFICATIONS ---------------- #

@login_required
def notifications(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    )

    notifications = []

    for job in jobs:

        if job.status == "Interview Scheduled":

            notifications.append(
                {
                    "title": "Interview Scheduled",
                    "message": f"{job.company_name} has scheduled your interview."
                }
            )

        elif job.status == "Selected":

            notifications.append(
                {
                    "title": "Congratulations 🎉",
                    "message": f"{job.company_name} has sent your offer letter."
                }
            )

        elif job.status == "Rejected":

            notifications.append(
                {
                    "title": "Application Update",
                    "message": f"Your application at {job.company_name} was rejected."
                }
            )

    return render(
        request,
        "tracker/notifications.html",
        {
            "notifications": notifications
        }
    )
    # ---------------- HR DASHBOARD ---------------- #

@login_required
def hr_dashboard(request):

    jobs = JobApplication.objects.all().order_by("-applied_date")

    return render(
        request,
        "tracker/hr_dashboard.html",
        {
            "jobs": jobs
        }
    )
# ---------------- VIEW CANDIDATE ---------------- #

@login_required
def view_candidate(request, id):

    job = get_object_or_404(JobApplication, id=id)

    profile, created = UserProfile.objects.get_or_create(
        user=job.user
    )

    if request.method == "POST":

        if "status" in request.POST:

            job.status = request.POST.get("status")
            job.save()

            messages.success(
                request,
                "Application status updated successfully."
            )

        elif "offer_letter" in request.FILES:

            job.offer_letter = request.FILES["offer_letter"]
            job.save()

            messages.success(
                request,
                "Offer Letter uploaded successfully."
            )

    return redirect("view_candidate", id=job.id)
