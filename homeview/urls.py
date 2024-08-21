from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from homeview import views

urlpatterns = [
    path('offerposter/', views.offerposter_list),
    path('offerposter1/', views.offerposter_list1),
    path('offerposter2/', views.offerposter_list2),
    path('offerposter3/', views.offerposter_list3),
]