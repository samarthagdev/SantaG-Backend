from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from address import views

urlpatterns = [
    path('address/', views.AddressView),

]