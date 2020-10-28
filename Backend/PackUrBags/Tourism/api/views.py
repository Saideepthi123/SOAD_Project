from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from authentication.models import UserData
from .serializers import UserDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from knox.models import AuthToken 



@api_view(['POST'])
def customer_login(request):
    data = request.data
    try:
        username = data['username']
        password = data['password']
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        user = UserData.objects.get(username=username, password=password)
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    try:
        user_token = AuthToken.objects.get(user=user)
    except:
        user_token = AuthToken.objects.create(user=user)[1]
    # print(user_token)
    return Response({
            'token': user_token,
            'user_id': user.user_id,
        })


@api_view(http_method_names=['GET', 'POST', ])
# @permission_classes([IsAuthenticated])
def user_list_view(request):
    if request.method == 'GET':
        return user_list_view_get(request)
    elif request.method == 'POST':
        return user_list_view_post(request)


def user_list_view_get(request):
    try:
        data = UserData.objects.all()
        serializer = UserDataSerializer(data, many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def user_list_view_post(request):
    user_data = JSONParser().parse(request)
    serializer = UserDataSerializer(data=user_data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def user_detail_view(request, slug):
    try:
        hdata = UserData.objects.get(user_id=slug)
        if request.method == 'GET':
            return user_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return user_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return user_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def user_detail_view_get(request, slug, hdata):
    serializer = UserDataSerializer(hdata)
    return Response(serializer.data)


def user_detail_view_put(request, slug, hdata):
    serializer = UserDataSerializer(hdata, data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def user_detail_view_delete(request, slug, hdata):
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message': 'succesfully deleted'}
    return Response(data)
