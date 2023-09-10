
from django.urls import path
from . import views

urlpatterns = [
    path('', views.english_course_list, name='english_course_list'),
]
