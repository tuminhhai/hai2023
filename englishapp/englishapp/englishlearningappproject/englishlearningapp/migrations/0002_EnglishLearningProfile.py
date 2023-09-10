

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('englishlearningapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishLearningProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=20)),
                ('lesson_progress', models.IntegerField(default=0)),
                ('last_lesson_completed', models.CharField(blank=True, max_length=50, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='englishlearningapp.students')),
            ],
        ),
    ]
