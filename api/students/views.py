from django.http import JsonResponse
from django.shortcuts import render
from .models import Student


def index(request):
    students = Student.objects.all()
    response = []
    for student in students:
        response.append({
            'name': student.name,
            'course': student.course,
            'rating': student.rating,
        })

    return JsonResponse(response, safe=False)
