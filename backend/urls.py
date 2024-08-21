"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend import settings

urlpatterns = [
    path('', include('restro.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('appapi.urls')),
    path('broadcast/', include('broadcast.urls')),
    path('das/', include('userdasboard.urls')),
    path('homeview/', include('homeview.urls')),
    path('bag/', include('bag.urls')),
    path('addr/', include('address.urls')),
    path('usercorrections/', include('changeaccount.urls')),
    path('menu/', include('menu1.urls')),
    path('firebase/', include('firbase.urls')),
    path('restro/', include('restro.urls')),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)