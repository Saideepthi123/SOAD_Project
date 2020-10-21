from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Tourism.models import UserData, GuideData
from .serializers import UserDataSerializer
# from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


@api_view(http_method_names=['GET','POST',])
# @permission_classes([IsAuthenticated])
def user_list_view(request):
    if request.method == 'GET':
        return user_list_view_get(request)
    elif request.method == 'POST':
        return user_list_view_post(request)

def user_list_view_get(request):
    try:
        data = User.objects.all()
        serializer = UserDataSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def user_list_view_post(request):
    serializer = UserDataSerializer(User, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET','PUT','DELETE'])
def user_detail_view(request, slug):
    try:
        hdata = User.objects.get(user_id = slug)
        if request.method == 'GET':
            return user_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return user_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return user_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def user_detail_view_get(request, slug, hdata):
    serializer = userDataSerializer(hdata)
    return Response(serializer.data)

def user_detail_view_put(request, slug, hdata):
    serializer = userDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def user_detail_view_delete(request, slug, hdata):
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message' : 'succesfully deleted'}
    return Response(data)


@api_view(http_method_names=['GET','PUT','DELETE'])
def guide_detail_view(request, slug):
    try:
        hdata = GuideData.objects.get(guide_id = slug)
        if request.method == 'GET':
            return user_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return user_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return user_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def guide_detail_view_get(request, slug, hdata):
    serializer = GuideDataSerializer(hdata)
    return Response(serializer.data)

def guide_detail_view_put(request, slug, hdata):
    serializer = GuideDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def guide_detail_view_delete(request, slug, hdata):
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message' : 'succesfully deleted'}
    return Response(data)

