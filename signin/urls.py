from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('grade/<int:pk>/', views.StudentsList.as_view(), name='students_list'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)