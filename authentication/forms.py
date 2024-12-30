from django import forms

from authentication.models import MyUserManager, Student


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['profile_pic','name','email','dept','phone_number','website']
        widgets = {
            "profile_pic": forms.FileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "dept": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "website": forms.TextInput(attrs={"class": "form-control"}),
        }
