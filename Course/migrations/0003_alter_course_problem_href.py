# Generated by Django 3.2.8 on 2021-11-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_alter_course_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='problem_href',
            field=models.TextField(default=''),
        ),
    ]
