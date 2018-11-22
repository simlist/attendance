from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('list/', views.List.as_view(), name='index'),
    path('grade/<int:pk>/', views.StudentsList.as_view(), name='students_list'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('line/<int:pk>/', views.LineDetail.as_view(), name='line_detail'),
    path('line/createline', views.CreateLine.as_view(), name='create_line'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
