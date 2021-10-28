from rest_framework import status
from icecream import ic
from admin.member.models import User
from admin.member.serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST', 'PUT'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        ic("VIEWS 에 GET 메소드입니다~")
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer, safe=False)
    elif request.method == 'POST':
        ic("VIEWS 에 POST 메소드입니다~")
        new_user = request.data['body']
        ic(new_user)
        serializer = UserSerializer(data=new_user['user'])
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        ic("VIEWS 에 PUT 메소드입니다~")
        return None

#
# @api_view(['GET', 'POST'])
# @parser_classes([JSONParser])
# def users(request, id):
#     pass


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    ic("views 에 로그인 메소드입니다~")
    new_user = request.data
    ic(new_user)
    serializer = UserSerializer(data=new_user)
    if serializer.is_valid():
        # serializer.save()
        return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)