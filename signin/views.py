from django.shortcuts import render

from rest_framework import generics
from rest_framework import mixins

from . import models
from . import serializers

# Create your views here.
def Home(request):
    return render(request, 'signin/index.html')


class GradesList(generics.ListCreateAPIView):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer


class StudentsList(generics.RetrieveAPIView):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer


class StudentDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class LineDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Line.objects.all()
    serializer_class = serializers.LineSerializer


class CreateLine(generics.CreateAPIView):
    serializer_class = serializers.LineSerializer
