# Generated by Django 5.1 on 2025-01-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_question_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_file',
            field=models.FileField(max_length=255, upload_to='get_upload_path'),
        ),
    ]
