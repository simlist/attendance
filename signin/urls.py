from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import apiurls

urlpatterns = [
    path('', views.Home, name='home'),
    path('api/', include(apiurls)),
]