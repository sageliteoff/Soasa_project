# Generated by Django 3.0.1 on 2020-01-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]