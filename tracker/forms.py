from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            "company_name",
            "job_role",
            "location",
            "salary",
            "resume",
            "applied_date",
        ]

        widgets = {
            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Company Name"
            }),

            "job_role": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Job Role"
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Job Location"
            }),

            "salary": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Expected Salary"
            }),

            "resume": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "applied_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            
        }

        labels = {
            "company_name": "Company Name",
            "job_role": "Job Role",
            "location": "Location",
            "salary": "Expected Salary",
            "resume": "Upload Resume (PDF /DOCX)",
            "applied_date": "Applied Date",
           
        }

    def clean_resume(self):
        resume = self.cleaned_data.get("resume")

        if resume:
            allowed = [".pdf", ".doc", ".docx"]

            if not any(resume.name.lower().endswith(ext) for ext in allowed):
                raise forms.ValidationError(
                    "Only PDF, DOC and DOCX files are allowed."
                )

        return resume