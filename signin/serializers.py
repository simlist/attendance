from rest_framework import serializers

from .models import Grade, Student, Line

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'last_name', 'first_name', 'grade')


class GradeSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Grade
        fields = ('id', 'name', 'students')

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ('date', 'student', 'time_in', 'in_signature',
                  'time_out', 'out_signature')
