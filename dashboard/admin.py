from django.contrib import admin

from dashboard.models import Question, UserAttribute

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["year", "semester", "exam_type", "department", "course_name"]
    list_filter = ["year", "semester", "exam_type", "department", "course_name"]
    search_fields = ["year", "semester", "exam_type", "department", "course_name"]


@admin.register(UserAttribute)
class UserAttributeAdmin(admin.ModelAdmin):
    list_display = ["user", "uploads", "downloads"]
    search_fields = ["user"]
