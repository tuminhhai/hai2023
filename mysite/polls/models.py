from django.db import models

#create your models here,
#model student
class student(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    grade = models.IntegerField()
    phone_numbers = models.CharField(max_length=20)

    def __str__(self):
      return self.name
