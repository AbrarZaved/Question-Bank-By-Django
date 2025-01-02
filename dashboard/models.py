import os
from platform import architecture
from django.db import models
from matplotlib.pyplot import summer
from numpy import real
import scipy as sp
from scipy.constants import year

# Create your models here.


class Question(models.Model):
    science_and_information_technology = "Science and Information Technology"
    business_and_entrepreneurship = "Business and Entrepreneurship"
    engineering = "Engineering"
    humanities_and_social_sciences = "Humanities and Social Sciences"
    health_and_life_sciences = "Health and Life Sciences"

    FACUTLY = [
        (science_and_information_technology, "Science and Information Technology"),
        (business_and_entrepreneurship, "Business and Entrepreneurship"),
        (engineering, "Engineering"),
        (humanities_and_social_sciences, "Humanities and Social Sciences"),
        (health_and_life_sciences, "Health and Life Sciences"),
    ]

    computer_science_and_engineering = "Computer Science and Engineering"
    software_engineering = "Software Engineering"
    Multimedia_and_creative_technology = "Multimedia and Creative Technology"
    computer_and_information_systems = "Computer and Information Systems"
    information_technology_and_management = "Information Technology and Management"

    DEPARTMENT_OF_SCIENCE_AND_INFORMATION_TECHNOLOGY = [
        (computer_science_and_engineering, "Computer Science and Engineering"),
        (software_engineering, "Software Engineering"),
        (Multimedia_and_creative_technology, "Multimedia and Creative Technology"),
        (computer_and_information_systems, "Computer and Information Systems"),
        (
            information_technology_and_management,
            "Information Technology and Management",
        ),
    ]

    business_administration = "Business Administration"
    tourism_and_hospitality_management = "Tourism and Hospitality Management"
    marketing = "Marketing"
    innovation_and_entrepreneurship = "Innovation and Entrepreneurship"
    finance_and_banking = "Finance and Banking"
    real_estate = "Real Estate"
    management = "Management"
    accounting = "Accounting"

    DEPARTMENT_OF_BUSINESS_AND_ENTREPRENEURSHIP = [
        (business_administration, "Business Administration"),
        (tourism_and_hospitality_management, "Tourism and Hospitality Management"),
        (marketing, "Marketing"),
        (innovation_and_entrepreneurship, "Innovation and Entrepreneurship"),
        (finance_and_banking, "Finance and Banking"),
        (real_estate, "Real Estate"),
        (management, "Management"),
        (accounting, "Accounting"),
    ]

    english = "English"
    law = "Law"
    journalism_media_and_communication = "Journalism, Media and Communication"
    development_studies = "Development Studies"
    information_scinece_and_library_management = (
        "Information Science and Library Management"
    )

    DEPARTMENT_OF_HUMANITIES_AND_SOCIAL_SCIENCES = [
        (english, "English"),
        (law, "Law"),
        (journalism_media_and_communication, "Journalism, Media and Communication"),
        (development_studies, "Development Studies"),
        (
            information_scinece_and_library_management,
            "Information Science and Library Management",
        ),
    ]

    information_and_communication_engineering = (
        "Information and Communication Engineering"
    )
    textile_engineering = "Textile Engineering"
    electrical_and_electronic_engineering = "Electrical and Electronic Engineering"
    civil_engineering = "Civil Engineering"
    architecture = "Architecture"

    DEPARTMENT_OF_ENGINEERING = [
        (
            information_and_communication_engineering,
            "Information and Communication Engineering",
        ),
        (textile_engineering, "Textile Engineering"),
        (
            electrical_and_electronic_engineering,
            "Electrical and Electronic Engineering",
        ),
        (civil_engineering, "Civil Engineering"),
        (architecture, "Architecture"),
    ]

    pharmacy = "Pharmacy"
    public_health = "Public Health"
    nutrition_and_food_engineering = "Nutrition and Food Engineering"
    agricultural_sciences = "Agricultural Sciences"
    environmental_science_and_disaster_management = (
        "Environmental Science and Disaster Management"
    )
    physical_education_and_sports_science = "Physical Education and Sports Science"
    genetic_engineering_and_biotechnology = "Genetic Engineering and Biotechnology"

    DEPARTMENT_OF_HEALTH_AND_LIFE_SCIENCES = [
        (pharmacy, "Pharmacy"),
        (public_health, "Public Health"),
        (nutrition_and_food_engineering, "Nutrition and Food Engineering"),
        (agricultural_sciences, "Agricultural Sciences"),
        (
            environmental_science_and_disaster_management,
            "Environmental Science and Disaster Management",
        ),
        (
            physical_education_and_sports_science,
            "Physical Education and Sports Science",
        ),
        (
            genetic_engineering_and_biotechnology,
            "Genetic Engineering and Biotechnology",
        ),
    ]

    summer = "Summer"
    fall = "Fall"
    spring = "Spring"
    all_semesters = "All"
    SEMESTER = [
        (all_semesters, "All"),
        (summer, "Summer"),
        (fall, "Fall"),
        (spring, "Spring"),
    ]

    mid_term = "Mid Term"
    final = "Final"

    EXAM_TYPE = [
        (mid_term, "Mid Term"),
        (final, "Final"),
    ]

    faculty = models.CharField(max_length=100, choices=FACUTLY)
    department = models.CharField(
        max_length=100
    )
    semester = models.CharField(max_length=100, choices=SEMESTER)
    exam_type = models.CharField(max_length=100, choices=EXAM_TYPE)
    course_name = models.CharField(max_length=100)
    year = models.IntegerField(default=2024)
    question_file = models.FileField(upload_to="get_upload_path", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_upload_path(instance, filename):
    # Sanitize the filename to prevent issues with special characters
        base, ext = os.path.splitext(filename)
        sanitized_name = base[:50] + ext  # Limit filename to 50 characters
        return (
            f"question/{instance.year}/{instance.exam_type}/"
            f"{instance.semester}/{instance.faculty}/{instance.department}/"
            f"{instance.course_name}/{sanitized_name}"
        )