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
        # ic("VIEWS 에 GET 메소드입니다~")
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        # ic(serializer.data)
        # ic(serializer.data)
        return JsonResponse(data=serializer.data, safe=False)
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
        # ic("VIEWS 에 PUT 메소드입니다~")
        mod_user = request.data
        ic(mod_user)
        # ic(mod_user.keys())
        dbUser = User.objects.get(pk=mod_user['username'])
        for i in mod_user.keys():
            dbUser.i = mod_user[i]
        # mod_serializer = UserSerializer(data=dbUser)
        # if mod_serializer.is_valid():
        dbUser.save()
        #     mod_serializer.save()
        return JsonResponse(data=dbUser, safe=False)


@api_view(['DELETE'])
def remove(request, username):
    print('Delete')
    # ic(request.GET.get(''))
    dbUser = User.objects.get(pk=username)
    dbUser.delete()
    return JsonResponse(data="탈퇴 성공", safe=False)


@api_view(['GET'])
def detail(request, username):
    print('*'*100)
    print('DETAIL')
    # ic(request.GET.get(''))
    ic(username)
    dbUser = User.objects.get(pk=username)
    userSerializer = UserSerializer(dbUser, many=False)
    return JsonResponse(data=userSerializer.data, safe=False)


@api_view(['POST'])
def login(request):
    try:
        loginUser = request.data
        # print(f'{type(loginUser)}') # <class 'dict'>
        ic(loginUser)
        dbUser = User.objects.get(pk = loginUser['username'])
        # print(f'{type(dbUser)}') # <class 'admin.user.models.User'>
        ic(dbUser)
        if loginUser['pwd'] == dbUser.pwd:
            print('******** 로그인 성공')
            userSerializer = UserSerializer(dbUser, many=False)
            ic(userSerializer)
            return JsonResponse(data=userSerializer.data, safe=False)
        else:
            print('******** 비밀번호 오류')
            return JsonResponse(data={'result':'PASSWORD-FAIL'}, status=201)

    except User.DoesNotExist:
        print('*' * 50)
        print('******** Username 오류')
        return JsonResponse(data={'result':'USERNAME-FAIL'}, status=201)