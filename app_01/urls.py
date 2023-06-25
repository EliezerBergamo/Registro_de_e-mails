# Imports

from django.urls import path
from app_01 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save, name='save'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]
