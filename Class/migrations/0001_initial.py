# Generated by Django 3.2.8 on 2021-11-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassHomework',
            fields=[
                ('className', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('class_homework', models.TextField()),
                ('class_course', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DataOfStudentInClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentUsername', models.CharField(max_length=50)),
                ('studentNumber', models.IntegerField(default=1)),
                ('className', models.CharField(max_length=50)),
                ('studentEmail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DataOfTeacherInClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherUsername', models.CharField(max_length=50)),
                ('teacherNumber', models.IntegerField(default=1)),
                ('className', models.CharField(max_length=50)),
                ('teacherEmail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InformationOfClass',
            fields=[
                ('className', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('classMaxSize', models.IntegerField(default=200)),
                ('canJoinOrNot', models.BooleanField(default=True)),
                ('introduction', models.CharField(default='', max_length=10000, null=True)),
            ],
        ),
    ]
