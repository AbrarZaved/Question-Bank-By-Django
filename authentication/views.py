import json
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect, render
from django.contrib import messages
from authentication.models import Student

def sign_in(request):
    if request.method=="POST":
        student_id=request.POST['student_id']
        password=request.POST['password']
        user=authenticate(student_id=student_id,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request, "authentication/authentication.html")


def register(request):
    if request.method=="POST":
        student_id=json.loads(request.body)['student_id']
        email=json.loads(request.body)['email']
        password=json.loads(request.body)['password']
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists.")
            return redirect('register')

        user=Student.objects.create_user(student_id=student_id,email=email,password=password)
        user.save()
    return render(request, "authentication/authentication.html")


def sign_out(request):
    logout(request)
    return redirect('sign_in')