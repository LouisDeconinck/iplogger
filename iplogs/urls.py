from django.urls import path
from . import views

urlpatterns = [
    path("", views.store_info, name="index"),
    path('store-info/', views.store_info, name='store_info'),
    path('store_location/', views.store_location, name='store_location'),
]