import json
from django.db.models import Q
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
    if faculty == "Science and Information Technology":
        department_choices = Question.DEPARTMENT_OF_SCIENCE_AND_INFORMATION_TECHNOLOGY
    elif faculty == "Business and Entrepreneurship":
        department_choices = Question.DEPARTMENT_OF_BUSINESS_AND_ENTREPRENEURSHIP
    elif faculty == "Engineering":
        department_choices = Question.DEPARTMENT_OF_ENGINEERING
    elif faculty == "Humanities and Social Sciences":
        department_choices = Question.DEPARTMENT_OF_HUMANITIES_AND_SOCIAL_SCIENCES
    elif faculty == "Health and Life Sciences":
        department_choices = Question.DEPARTMENT_OF_HEALTH_AND_LIFE_SCIENCES

    return JsonResponse({"departments": department_choices})


def question_results(request):
    data = json.loads(request.body)

    faculty = data.get("faculty").strip()
    department = data.get("department").strip()
    semester = data.get("semester").strip()
    exam_type = data.get("exam_type").strip()
    course_name = data.get("course_name").strip()
    year = data.get("year")

    questions = Question.objects.filter(
        faculty=faculty,
        department=department,
        semester=semester,
        exam_type=exam_type,
        course_name=course_name,
        year=year,
    )
    return JsonResponse(list(questions.values()), safe=False)


def contribute(request):
    question_form = QuestionForm()
    return render(
        request, "dashboard/contribute.html", {"question_form": question_form}
    )


def upload_questions(request):
    if request.method == "POST":
        faculty = request.POST.get("faculty", "").strip()
        department = request.POST.get("department", "").strip()
        semester = request.POST.get("semester", "").strip()
        exam_type = request.POST.get("exam_type", "").strip()
        course_name = request.POST.get("course_name", "").strip()
        year = request.POST.get("year")
        question_file = request.FILES.get("question_file")  # Handle file upload

        # Save the Question object
        question = Question.objects.create(
            faculty=faculty,
            department=department,
            semester=semester,
            exam_type=exam_type,
            course_name=course_name,
            year=year,
            question_file=question_file,  # Save the file
        )
        question.save()

        return JsonResponse({"Question Saved": "successful"}, safe=False)
    return JsonResponse({"error": "Invalid request method"}, status=400)
