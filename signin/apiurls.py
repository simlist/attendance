from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (GradesList,
                    StudentsList,
                    StudentDetail,
                    LineDetail,
                    CreateLine)

urlpatterns = [
    path('gradeslist/', GradesList.as_view()),
    path('studentslist/', StudentsList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('line/<int:pk>/', LineDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)