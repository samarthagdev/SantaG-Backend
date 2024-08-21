from rest_framework.urlpatterns import format_suffix_patterns
from userdasboard import views
from django.urls import path
urlpatterns = [
    path('userdaspage/', views.userdaspage),
]

urlpatterns = format_suffix_patterns(urlpatterns)