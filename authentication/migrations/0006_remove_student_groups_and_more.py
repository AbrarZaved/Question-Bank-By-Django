# Generated by Django 5.1 on 2025-01-06 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_student_cover_pic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user_permissions',
        ),
    ]
