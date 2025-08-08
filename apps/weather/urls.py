from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='weather'),  #the path for index view
    path('delete/<int:pk>/', views.city_delete, name='city_delete'),
]