
from django.shortcuts import render
from .models import EnglishCourse

def english_course_list(request):
    courses = EnglishCourse.objects.all()
    return render(request, 'english_course_list.html', {'courses': courses})
