from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from appapi import views
from cosmatic.models import Cosmaticitems
from .serializers import CosmaticSerilizer

urlpatterns = [
    path('cosmatic/', views.cosmatic_list),
    path('cosmaticsearch/', views.UserListView.as_view()),
    path('cosmatic/<cosToken>/', views.cosmatic_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)