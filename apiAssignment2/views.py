# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Moisture
from .serializer import MoistureSerializer
from .datasheet import plant_sheet


PLANT_TYPE = { 'plant1': 'pothos', 'plant2': 'pothos'}

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
def get_recent(request, plantId):
    try:
        entry = Moisture.objects.filter(plant_id=plantId).last()
        serializer = MoistureSerializer(entry)

        pType = serializer.data['plant_type']
        detail = {
            'id': serializer.data['id'],
            'plant_id': serializer.data['plant_id'],
            'level': serializer.data['level'],
            'created': serializer.data['created'],
            'plant_type': pType,
            'ideal_level': plant_sheet[pType]['level'],
            'desc': plant_sheet[pType]['desc']
        }
        return Response(detail, status=status.HTTP_200_OK)
    except Moisture.DoesNotExist:
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

@api_view(['GET'])
def change_plant(request, plantId, plantType):
    try:
        PLANT_TYPE[plantId] = plantType
        res = {
            'plant_type': PLANT_TYPE[plantId],
            'desc': plant_sheet[plantType]['desc']
        }
        return Response(res, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_plants(request):
    try:
        arr = plant_sheet.keys()
        return Response(arr, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def insert_item(request):
    id = request.data['plant_id']
    
    plant = {
        'plant_type': PLANT_TYPE[id],
        'plant_id': request.data['plant_id'],
        'level': request.data['level']
    }
    
    serializer = MoistureSerializer(data=plant)

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
