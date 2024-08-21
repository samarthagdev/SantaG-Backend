from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url('otpchecking', views.otp_checking, name="otpchecking"),
    url('forgototp', views.otp_checking1, name="otpchecking1"),
    url('verification', views.otp_verification, name="verification"),
    url('login', obtain_auth_token, name="login"),
    url('hellow1', views.otp_verification1, name="verification1"),
    url('landingpage', views.landingpage, name="landingpage"),
    url('sellerchecker', views.sellerchecker, name="landingpage1"),
    url('santaorder', views.santaorder, name="Santaorder"),
]