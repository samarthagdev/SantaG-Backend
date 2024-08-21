from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from bag import views
from .models import BagAdding
from .serializers import BagAddingSerilizer

urlpatterns = [
    path('BagAdding/', views.BagView),
    path('itemsBag/', views.ItemsView),
    path('myorder/', views.MyOrder),
    path('addtocart/', views.CartView),
    path('removeitems/', views.RemoveItemsView),
]

urlpatterns = format_suffix_patterns(urlpatterns)