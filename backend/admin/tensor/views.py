from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.tensor.models import Calculator, FashionClassification, TensorFunction


@api_view(['GET'])
@parser_classes([JSONParser])
def calculate(request):
    Calculator().process()
    return JsonResponse({'calculator': 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def fashion(request):
    FashionClassification().fashion()
    return JsonResponse({'Fashion Classification': 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def tf_function(request):
    TensorFunction().tf_function()
    return JsonResponse({'Tensor Function': 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def hook(request):
    TensorFunction().hook()
    return JsonResponse({'Hook': 'Success'})

