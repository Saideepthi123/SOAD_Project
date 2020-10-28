from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from guide.models import GuideData
from .serializers import GuideDataSerializer
from django.core.exceptions import ObjectDoesNotExist


@api_view(http_method_names=['GET', 'POST', ])
# @permission_classes([IsAuthenticated])
def guide_list_view(request):
    if request.method == 'GET':
        return guide_list_view_get(request)
    elif request.method == 'POST':
        return guide_list_view_post(request)


def guide_list_view_get(request):
    try:
        data = GuideData.objects.all()
        serializer = GuideDataSerializer(data, many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def guide_list_view_post(request):
    guide_data = JSONParser().parse(request)
    serializer = GuideDataSerializer(data=guide_data)
    print(serializer, "hi")
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def guide_detail_view(request, slug):
    try:
        hdata = GuideData.objects.get(guide_id=slug)
        if request.method == 'GET':
            return guide_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return guide_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return guide_detail_view_delete(request, slug, hdata)
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
        data = {'message': 'successfully deleted'}
    return Response(data)
