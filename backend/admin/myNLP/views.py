from django.http.response import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.myNLP.models import Imdb, NaverMovie


@api_view(['GET'])
@parser_classes([JSONParser])
def imdb_process(request):
    Imdb().process()
    return JsonResponse({'Imdb Process': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMovie().naver_process()
    return JsonResponse({'Naver Process': 'SUCCESS'})
