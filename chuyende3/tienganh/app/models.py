from django.db import models

class Students(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    grade = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class EnglishCourse(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # lessons = models.ManyToManyField('EnglishLesson')

    def __str__(self):
        return self.title

class EnglishLearningProfile(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE)
    english_level = models.CharField(max_length=20, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    lesson_progress = models.IntegerField(default=0)
    last_lesson_completed = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.student.name + "'s English Learning Profile"




