from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.myGAN.models import AutoencodersGans, GenerateFashion

@api_view(['GET'])
@parser_classes([JSONParser])
def autoencoderGans_process(request):
    AutoencodersGans().process()
    return JsonResponse({'AutoencoderGans': 'Success'})

