from django.urls import path
from . import views
urlpatterns = [
    path('', views.api_overview, name="ApiOverview"),
    path('getMoistureLevels/', views.get_items, name="getMoistureLevels"),
    path('getMoistureLevel/<str:pk>/', views.get_item, name="getMoistureLevel"),
    path('insertMoistureLevel/', views.insert_item, name="insertMoistureLevel"),
    path('updateMoistureLevel/<str:pk>/', views.update_item, name="updateMoistureLevel"),
    path('deleteMoistureLevel/<str:pk>/', views.delete_item, name="deleteMoistureLevel"),
]