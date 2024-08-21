from django.conf.urls import url
from . import views

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    url('usercorrection', views.UserCorrections, name="usercorrection"),
    url('Setpass', views.Setpass, name="Setpass"),

]
