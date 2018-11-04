from rest_framework import serializers

from .models import Grade, Student, Line

class GradeSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Grade
        fields = ('id', 'name', 'students')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'last_name', 'first_name', 'grade') 

