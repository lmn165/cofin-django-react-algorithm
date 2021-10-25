from django.http.response import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.nlp.models import Imdb


@api_view(['GET'])
@parser_classes([JSONParser])
def imdb_process(request):
    Imdb().process()
    return JsonResponse({'Imdb Process': 'SUCCESS'})
