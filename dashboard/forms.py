from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "faculty",
            "department",
            "semester",
            "exam_type",
            "course_name",
            "year",
            "question_file",
        ]

        widgets = {
            "faculty": forms.Select(attrs={"class": "custom-select"}),
            "department": forms.Select(attrs={"class": "custom-select"}),
            "semester": forms.Select(),
            "exam_type": forms.Select(),
            "course_name": forms.TextInput(
                attrs={"class": "custom-input", "placeholder": "Enter Course Name"}
            ),
            "year": forms.NumberInput(
                attrs={"class": "custom-input", "placeholder": "Enter Year"}
            ),
            "question_file": forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial department choices based on the faculty
        self.fields["department"].queryset = self.get_department_choices(
            self.initial.get("faculty")
        )

        # Add an empty option manually for each ChoiceField (faculty, department, semester, exam_type)
        for field_name in ["faculty", "department", "semester", "exam_type"]:
            field = self.fields.get(field_name)
            if isinstance(field, forms.ChoiceField):
                field.choices = list(field.choices)

    def get_department_choices(self, faculty):
        """Return department choices based on selected faculty"""
        if faculty == Question.science_and_information_technology:
            return Question.DEPARTMENT_OF_SCIENCE_AND_INFORMATION_TECHNOLOGY
        elif faculty == Question.business_and_entrepreneurship:
            return Question.DEPARTMENT_OF_BUSINESS_AND_ENTREPRENEURSHIP
        elif faculty == Question.engineering:
            return Question.DEPARTMENT_OF_ENGINEERING
        elif faculty == Question.humanities_and_social_sciences:
            return Question.DEPARTMENT_OF_HUMANITIES_AND_SOCIAL_SCIENCES
        elif faculty == Question.health_and_life_sciences:
            return Question.DEPARTMENT_OF_HEALTH_AND_LIFE_SCIENCES
        return []
