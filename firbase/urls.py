from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from firbase import views


urlpatterns = [
    path('firebasetoken/', views.firebasetoken),
]

urlpatterns = format_suffix_patterns(urlpatterns)