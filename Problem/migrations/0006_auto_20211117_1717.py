# Generated by Django 3.2.8 on 2021-11-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problem', '0005_auto_20211117_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='input',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='output',
            field=models.TextField(default=''),
        ),
    ]
