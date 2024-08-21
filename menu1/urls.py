from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from menu1 import views

urlpatterns = [
    path('card/', views.Menu_details),
]