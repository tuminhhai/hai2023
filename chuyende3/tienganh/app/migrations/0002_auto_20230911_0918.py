# Generated by Django 3.2.21 on 2023-09-11 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='englishcourse',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='englishcourse',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='englishcourse',
            name='level',
        ),
        migrations.RemoveField(
            model_name='englishcourse',
            name='price',
        ),
        migrations.RemoveField(
            model_name='englishcourse',
            name='start_date',
        ),
    ]
