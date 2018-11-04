from django.shortcuts import render

from rest_framework import generics
from rest_framework import mixins

from . import models
from . import serializers

# Create your views here.
def index(generics.ListCreateAPIView):
    query_set = Grade.objects.all()
    serializer_class = serializers.GradeSerializer
