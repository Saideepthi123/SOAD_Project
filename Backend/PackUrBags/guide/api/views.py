from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from guide.models import GuideData
from monuments.models import Monument
from .serializers import GuideDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView


class GuideList(APIView):

    def get(self, request):
        try:
            data = GuideData.objects.all()
            serializer = GuideDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        guide_data = JSONParser().parse(request)
        serializer = GuideDataSerializer(data=guide_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GuideDetail(APIView):

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
        data = {'message': 'error during deletion'}
        if delresult[0] == 1:
            data = {'message': 'successfully deleted'}
        return Response(data)


class GuidePlace(APIView):
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
