from django.contrib import admin
from django.urls import path
from .views import home, CityDetailView, CityCreateView, CityDeleteView, CityUpdateView

urlpatterns = [
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='add'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('', home, name='home'),
]
