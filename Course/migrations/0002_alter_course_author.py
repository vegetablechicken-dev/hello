# Generated by Django 3.2.8 on 2021-11-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.CharField(default='admin', max_length=50, null=True),
        ),
    ]
