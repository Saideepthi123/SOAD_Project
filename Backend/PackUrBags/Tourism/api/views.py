from knox.models import AuthToken 
from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from authentication.models import UserData
from .serializers import UserDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from test.test_import import data
from rest_framework.views import APIView


class UserList(APIView):
    def get(self, request):
        try:
            data = UserData.objects.all()
            serializer = UserDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        User_data = JSONParser().parse(request)
        serializer = UserDataSerializer(data=User_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request, slug):
        hdata = UserData.objects.get(user_id=slug)
        serializer = UserDataSerializer(hdata)
        return Response(serializer.data)

    def put(self, request, slug):
        hdata = UserData.objects.get(user_id=slug)
        serializer = UserDataSerializer(hdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        hdata = UserData.objects.get(user_id=slug)
        delresult = hdata.delete()
        data = {'message': 'error during deletion'}
        if delresult[0] == 1:
            data = {'message': 'successfully deleted'}
        return Response(data)
