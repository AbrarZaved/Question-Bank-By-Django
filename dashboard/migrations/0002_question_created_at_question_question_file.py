# Generated by Django 5.1 on 2024-12-30 17:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='question/<django.db.models.fields.IntegerField>/<django.db.models.fields.CharField>/<django.db.models.fields.CharField>/<django.db.models.fields.CharField>/<django.db.models.fields.CharField>/<django.db.models.fields.CharField>/'),
            preserve_default=False,
        ),
    ]
