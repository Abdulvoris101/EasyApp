from django.shortcuts import render
from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
