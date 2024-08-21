
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('adminlogin', views.admin_login, name="AdminLogin"),
    url('employeelogin', views.employee_login, name="EmployeeLogin"),
    url('openinglogin', views.opening_login, name="OpeningLogin"),
    url('addingemployee', views.adding_employee, name="AddingEmployee"),
    url('addingcategory', views.adding_category, name="AddingCategory"),
    path('category/', views.getting_category),
    path('items/', views.getting_items),
    url('removingboth', views.removing_category, name="RemovingCategory"),
    url('addingitems', views.adding_items, name="AddingItems"),
    url('previousdata', views.getting_previousData, name="PreviousData")
]
