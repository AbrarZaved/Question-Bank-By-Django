from django import forms

from authentication.models import MyUserManager, Student


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "student_id": forms.TextInput(attrs={"class": "form-control"}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control"}),
            "cover_pic": forms.FileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "dept": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "social_media_handle": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.HiddenInput(),
            "is_admin": forms.HiddenInput(),
            "is_staff": forms.HiddenInput(),
        }
