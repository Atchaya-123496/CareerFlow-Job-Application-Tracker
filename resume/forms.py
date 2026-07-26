from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume

        fields = [
            "full_name",
            "email",
            "phone",
            "summary",
            "education",
            "skills",
            "projects",
            "experience",
            "linkedin",
            "github",
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "summary": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "education": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "skills": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "projects": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "experience": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "linkedin": forms.URLInput(attrs={
                "class": "form-control"
            }),

            "github": forms.URLInput(attrs={
                "class": "form-control"
            }),
        }