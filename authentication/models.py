from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, student_id, password=None, **extra_fields):
        if not student_id:
            raise ValueError("Student ID must be set")

        user = self.model(student_id=student_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_admin"):
            raise ValueError("Superuser must have is_admin=True.")
        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(student_id, password, **extra_fields)


class Student(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=50, unique=True)
    profile_pic=models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    dept = models.CharField(max_length=50, blank=True)
    phone_number=models.CharField(max_length=50,blank=True)
    website=models.CharField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # You can modify related_name to avoid clashes with the default Django User model.
    groups = None
    user_permissions = None

    objects = MyUserManager()

    USERNAME_FIELD = "student_id"
    REQUIRED_FIELDS = []  # List additional required fields here, if any

    def __str__(self):
        return self.student_id
