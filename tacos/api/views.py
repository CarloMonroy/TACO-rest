from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PlacesSerializer
from .models import Places

# Create your views here

def places_list_view(request):
    #get all places
    places = Places.objects.all()
    #serialize them
    serializer = PlacesSerializer(places, many=True)
    #return json
    return JsonResponse({'all_places':serializer.data})

