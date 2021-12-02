from django.urls import path
from . import views
urlpatterns = [
    path('', views.api_overview, name="ApiOverview"),
    path('getMoistureLevels/<str:plantId>/', views.get_items, name="getMoistureLevels"),
    path('getMoistureLevel/<str:id>/', views.get_item, name="getMoistureLevel"),
#     path('getRecentMoistureLevel/', views.get_recent, name="getRecentMoistureLevel"),
    path('getRecentMoistureLevels/<str:plantId>/', views.get_recents, name="getRecentMoistureLevels"),
    path('insertMoistureLevel/', views.insert_item, name="insertMoistureLevel"),
    path('updateMoistureLevel/<str:pk>/', views.update_item, name="updateMoistureLevel"),
    path('deleteMoistureLevel/<str:pk>/', views.delete_item, name="deleteMoistureLevel"),
]
