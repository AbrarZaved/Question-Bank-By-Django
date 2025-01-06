import json
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from authentication.forms import ProfileForm
from authentication.models import Student


def sign_in(request):
    if request.method == "POST":
        student_id = request.POST["student_id"]
        password = request.POST["password"]
        user = authenticate(student_id=student_id, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "authentication/authentication.html")


def register(request):
    if request.method == "POST":
        student_id = json.loads(request.body)["student_id"]
        email = json.loads(request.body)["email"]
        password = json.loads(request.body)["password"]
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists.")
            return redirect("register")

        user = Student.objects.create_user(
            student_id=student_id, email=email, password=password
        )
        user.save()
    return render(request, "authentication/authentication.html")


@login_required
def profile(request):
    user = request.user
    profile_form = ProfileForm(instance=user)
    return render(
        request,
        "authentication/profile.html",
        {"profile_form": profile_form, "user": user},
    )


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("profile")
    return redirect("profile")


@login_required
def view_profile(request, boom):
    user = Student.objects.get(pk=boom)
    return render(request, "authentication/view_profile.html", {"user": user})


def sign_out(request):
    logout(request)
    return redirect("sign_in")
