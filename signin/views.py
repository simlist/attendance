from django.shortcuts import render

from rest_framework import generics
from rest_framework import mixins

from . import models
from . import serializers

# Create your views here.
class Index(generics.ListCreateAPIView):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer

class StudentsList(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer