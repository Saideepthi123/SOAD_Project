from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from monuments.models import Monument, MonumentInfo, City 
from .serializers import MonumentDataSerializer, MonumentInfoDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from test.test_import import data
from rest_framework.views import APIView
from .serializers import CityDataSerializer, MonumentInfoDataSerializer


class MonumentList(APIView):
    def get(self, request):
        try:
            data = Monument.objects.all()
            serializer = MonumentDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        Monument_data = JSONParser().parse(request)
        serializer = MonumentDataSerializer(data=Monument_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MonumentDetail(APIView):
    def get(self, request, slug):
        try:
            hdata = Monument.objects.get(monument_id=slug)
            serializer = MonumentDataSerializer(hdata)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        hdata = Monument.objects.get(monument_id=slug)
        serializer = MonumentDataSerializer(hdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        hdata = Monument.objects.get(monument_id=slug)
        delresult = hdata.delete()
        data = {'message': 'error during deletion'}
        if delresult[0] == 1:
            data = {'message': 'successfully deleted'}
        return Response(data)

class MonumentInfoList(APIView):
    def get(self, request):
        try:
            data = MonumentInfo.objects.all()
            serializer = MonumentInfoDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        Monument_data = JSONParser().parse(request)
        serializer = MonumentInfoDataSerializer(data=Monument_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MonumentInfoDetail(APIView):
    def get(self, request):
        try:
            place = request.GET['monument']
            place = place.lower()
            place_id = 0
            for m in MonumentInfo.objects.all():
                if m.monument_name.lower() == place:
                    place_id = m.monument_info_id
                    break

            hdata = MonumentInfo.objects.filter(monument_info_id=place_id)
            serializer = MonumentInfoDataSerializer(hdata, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CityList(APIView):
    def get(self, request):
        try:
            data = City.objects.all()
            serializer = CityDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        city_data = JSONParser().parse(request)
        serializer = CityDataSerializer(data=city_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CityDetail(APIView):
    def get(self, request, slug):
        try:
            hdata = City.objects.get(city_id=slug)
            serializer = CityDataSerializer(hdata)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        hdata = City.objects.get(city_id=slug)
        serializer = CityDataSerializer(hdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        hdata = City.objects.get(city_id=slug)
        delresult = hdata.delete()
        data = {'message': 'error during deletion'}
        if delresult[0] == 1:
            data = {'message': 'successfully deleted'}
        return Response(data)
    	