# Generated by Django 3.2.8 on 2021-11-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problem', '0003_alter_problem_problem_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='input1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='input2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='input3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='input4',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='input5',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='output1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='output2',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='output3',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='output4',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='output5',
            field=models.TextField(default=''),
        ),
    ]
