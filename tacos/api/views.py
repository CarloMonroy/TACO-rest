from .serializers import PlacesSerializer
from .models import Places
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here
@api_view(['GET', 'POST'])
def places_list_view(request, format=None):
    if request.method == 'GET':
        #get all places
        places = Places.objects.all()
        #serialize them
        serializer = PlacesSerializer(places, many=True)
        #return json
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PlacesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def places_detail(request, id, format=None):

    try:
        place = Places.objects.get(pk=id)
    except Places.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlacesSerializer(place)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlacesSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)