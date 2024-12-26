from django.contrib import admin
from django.contrib.auth.models import Group
from authentication.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_id','name','email','phone_number','dept']
    list_filter=['dept']
    search_fields=['student_id']
    list_per_page=10

admin.site.unregister(Group)
