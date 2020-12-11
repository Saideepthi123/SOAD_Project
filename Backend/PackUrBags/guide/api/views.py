from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from guide.models import GuideData
from monuments.models import Monument, City
from .serializers import GuideDataSerializer, SearchGuideSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from datetime import datetime


class SearchGuides(generics.GenericAPIView):
    serializer_class = SearchGuideSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data)
        data = serializer.data
        city = City.objects.get(city_name=data['city'])
        monuments = city.monuments.all()
        self.queryset = GuideData.objects.filter(place__in=monuments)
        date = datetime.strptime(data['start_date'], '%Y-%m-%d')
        start_date = datetime(date.year, date.month, date.day).date()
        available_guides = []
        for i in range(len(self.queryset)):
            guide = self.queryset[i]
            if GuideData.is_available(guide, start_date) is True:
                available_guides.append(guide)
        serializer = GuideDataSerializer(available_guides, many=True)
        return Response(serializer.data)


class GuideList(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = GuideData.objects.all()
            serializer = GuideDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        guide_data = JSONParser().parse(request)
        serializer = GuideDataSerializer(data=guide_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GuideDetail(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        hdata = GuideData.objects.get(guide_id=slug)
        serializer = GuideDataSerializer(hdata)
        return Response(serializer.data)

    def put(self, request, slug):
        hdata = GuideData.objects.get(guide_id=slug)
        serializer = GuideDataSerializer(hdata, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        hdata = GuideData.objects.get(guide_id=slug)
        delresult = hdata.delete()
        data = {'message': 'Error during deletion'}
        if delresult[0] == 1:
            data = {'message': 'Successfully deleted'}
        return Response(data)


class GuidePlace(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            place = request.GET['place']
            place = place.lower()
            place_id = 0
            for m in Monument.objects.all():
                if m.monument_name.lower() == place:
                    place_id = m.monument_id
                    break

            hdata = GuideData.objects.filter(place=place_id)
            serializer = GuideDataSerializer(hdata, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
