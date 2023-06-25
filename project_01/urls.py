# Imports

from django.contrib import admin
from django.urls import path, include
from app_01 import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('app/', include('app_01.urls'))
]
