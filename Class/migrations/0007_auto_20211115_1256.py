# Generated by Django 3.2.8 on 2021-11-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0006_auto_20211115_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classhomework',
            name='className',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='classhomework',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
