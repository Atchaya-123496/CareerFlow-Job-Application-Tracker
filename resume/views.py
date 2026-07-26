from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Resume
from .forms import ResumeForm
from django.http import HttpResponse
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


@login_required
def resume_builder(request):

    resume, created = Resume.objects.get_or_create(
        user=request.user,
        defaults={
            "full_name": request.user.get_full_name() or request.user.username,
            "email": request.user.email,
        }
    )

    if request.method == "POST":

        form = ResumeForm(
            request.POST,
            instance=resume
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Resume saved successfully."
            )

            return redirect("resume")

    else:

        form = ResumeForm(instance=resume)

    return render(
        request,
        "resume/resume_builder.html",
        {
            "form": form
        }
    )
@login_required
def resume_preview(request):

    resume = Resume.objects.get(user=request.user)

    return render(
        request,
        "resume/resume_preview.html",
        {
            "resume": resume
        }
    )

@login_required
def download_resume_pdf(request):

    resume = Resume.objects.get(user=request.user)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Resume.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph(f"<b>{resume.full_name}</b>", styles["Title"]))
    story.append(Paragraph(f"Email: {resume.email}", styles["Normal"]))
    story.append(Paragraph(f"Phone: {resume.phone}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Professional Summary</b>", styles["Heading2"]))
    story.append(Paragraph(resume.summary or "-", styles["Normal"]))

    story.append(Paragraph("<b>Education</b>", styles["Heading2"]))
    story.append(Paragraph(resume.education or "-", styles["Normal"]))

    story.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
    story.append(Paragraph(resume.skills or "-", styles["Normal"]))

    story.append(Paragraph("<b>Projects</b>", styles["Heading2"]))
    story.append(Paragraph(resume.projects or "-", styles["Normal"]))

    story.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
    story.append(Paragraph(resume.experience or "-", styles["Normal"]))

    story.append(Paragraph("<b>LinkedIn</b>", styles["Heading2"]))
    story.append(Paragraph(resume.linkedin or "-", styles["Normal"]))

    story.append(Paragraph("<b>GitHub</b>", styles["Heading2"]))
    story.append(Paragraph(resume.github or "-", styles["Normal"]))

    doc.build(story)

    return response