from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime.models import CrimeCctvModel


@api_view(['GET'])
@parser_classes([JSONParser])
def crime_model(request):
    CrimeCctvModel().create_crime_model()
    return JsonResponse({'result': 'Crime Info Success'})


def police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'result': 'Police Position Success'})
