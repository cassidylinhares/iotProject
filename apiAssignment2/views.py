# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import Moisture
from .serializer import MoistureSerializer


@api_view(['GET'])
def api_overview(request):
    data = {
        "all_entries": "getMoistureLevels/<str:plantId/",
        "single_entry": "getMoistureLevel/<str:pk>/",
        "recent_entry": 'getRecentMoistureLevels/<str:plantId>/',
        "create_entry": "insertMoistureLevel/",
        "update_entry": "updateMoistureLevel/<str:pk>/",
        "delete_entry": "deleteMoistureLevel/<str:pk>/",
    }
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_items(request, plantId):
    try:
        entries = Moisture.objects.filter(plant_id=plantId)
        serializer = MoistureSerializer(entries, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Moisture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_item(request, id):
    try:
        entry = Moisture.objects.get(id=id)
        serializer = MoistureSerializer(entry)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Moisture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_recent(request):
    try:
        res = requests.get('http://192.168.0.150/').json()
        return Response(res, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_recents(request, plantId):
    try:
        entries = Moisture.objects.filter(
            plant_id=plantId).order_by('-created')
        serializer = MoistureSerializer(entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Moisture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def insert_item(request):
    serializer = MoistureSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_item(request, pk):
    try:
        entry = Moisture.objects.get(id=pk)
        serializer = MoistureSerializer(instance=entry, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        entry = Moisture.objects.get(id=pk)
        entry.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
