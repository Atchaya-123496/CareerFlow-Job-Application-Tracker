from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = [
            "profile_photo",
            "phone",
            "address",
            "education",
            "skills",
            "linkedin",
            "github",
            "company",
        ]

        widgets = {

            "profile_photo": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Phone Number"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Enter Address"
            }),

            "education": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "B.E Computer Science Engineering"
            }),

            "skills": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Python, SQL, Excel, Power BI"
            }),

            "linkedin": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://linkedin.com/in/username"
            }),

            "github": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://github.com/username"
            }),

            "company": forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Company Name (HR only)"
             }),
        }


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Username"
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Email Address"
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Password"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm Password"
        })
    )
    role = forms.ChoiceField(
    choices=UserProfile.ROLE_CHOICES,
    widget=forms.Select(attrs={
        "class": "form-control"
    })
)

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user