from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.member.models import Member
from admin.member.serializer import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        print("VIEWS 에 GET 메소드입니다~")
        all_users = Member.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer, safe=False)
    elif request.method == 'POST':
        print("VIEWS 에 POST 메소드입니다~")
        new_user = request.data['body']
        print(new_user)
        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)