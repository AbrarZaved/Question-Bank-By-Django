import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Question
from dashboard.forms import QuestionForm


# Create your views here.
def index(request):
    question_form = QuestionForm()
    return render(request, "dashboard/index.html", {"question_form": question_form})


def get_departments(request):
    faculty = json.loads(request.body).get("faculty")
    department_choices = []
    print(faculty)
    if faculty == "science_and_information_technology":
        department_choices = Question.DEPARTMENT_OF_SCIENCE_AND_INFORMATION_TECHNOLOGY
    elif faculty == "business_and_entrepreneurship":
        department_choices = Question.DEPARTMENT_OF_BUSINESS_AND_ENTREPRENEURSHIP
    elif faculty == "engineering":
        department_choices = Question.DEPARTMENT_OF_ENGINEERING
    elif faculty == "humanities_and_social_sciences":
        department_choices = Question.DEPARTMENT_OF_HUMANITIES_AND_SOCIAL_SCIENCES
    elif faculty == "health_and_life_sciences":
        department_choices = Question.DEPARTMENT_OF_HEALTH_AND_LIFE_SCIENCES

    return JsonResponse({"departments": department_choices})


def question_results(request):
    faculty=json.loads(request.body).get("faculty")
    department=json.loads(request.body).get("department")
    semester=json.loads(request.body).get("semester")
    exam_type=json.loads(request.body).get("exam_type")
    course_name=json.loads(request.body).get("course_name")
    year=json.loads(request.body).get("year")