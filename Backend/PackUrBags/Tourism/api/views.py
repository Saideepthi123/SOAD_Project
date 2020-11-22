import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from authentication.models import UserData
from Tourism.models import Booking, Payment, UserHistory
from .serializers import UserDataSerializer, BookingDataSerializer, PaymentDataSerializer, UserHistoryDataSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = UserData.objects.get(user_id=slug)
            serializer = UserDataSerializer(hdata)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        try:
            hdata = UserData.objects.get(user_id=slug)
            serializer = UserDataSerializer(hdata, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def delete(self, request, slug):
        try:
            hdata = UserData.objects.get(user_id=slug)
            delresult = hdata.delete()
            data = {}
            if delresult[0] == 1:
                data = {'message': 'successfully deleted'}
            return Response(data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class BookingList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = Booking.objects.all()
            serializer = BookingDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        Booking_data = JSONParser().parse(request)
        serializer = BookingDataSerializer(data=Booking_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class BookingDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = Booking.objects.get(booking_id=slug)
            serializer = BookingDataSerializer(hdata)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug):
        try:
            hdata = Booking.objects.get(booking_id=slug)
            serializer = BookingDataSerializer(hdata, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        try:
            hdata = Booking.objects.get(booking_id=slug)
            delresult = hdata.delete()
            data = {'message': 'error during deletion'}
            if delresult[0] == 1:
                data = {'message': 'successfully deleted'}
            return Response(data)

        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class BookingDetailUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = Booking.objects.filter(user_email=slug)
            serializer = BookingDataSerializer(hdata, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class BookingDetailGuide(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = Booking.objects.filter(guide_email=slug)
            serializer = BookingDataSerializer(hdata, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class PaymentList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = Payment.objects.all()
            serializer = PaymentDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        payment_data = JSONParser().parse(request)
        serializer = PaymentDataSerializer(data=payment_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PaymentDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = Payment.objects.get(payment_id=slug)
            serializer = PaymentDataSerializer(hdata)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        try:
            hdata = Payment.objects.get(payment_id=slug)
            serializer = PaymentDataSerializer(hdata, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        try:
            hdata = Payment.objects.get(payment_id=slug)
            delresult = hdata.delete()
            data = {'message': 'error during deletion'}
            if delresult[0] == 1:
                data = {'message': 'successfully deleted'}
            return Response(data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = Payment.objects.filter(user_email=slug)
            serializer = PaymentDataSerializer(hdata, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class PaymentDetailGuide(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = Payment.objects.filter(guide_email=slug)
            serializer = PaymentDataSerializer(hdata, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class UserHistoryList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = UserHistory.objects.all()
            serializer = UserHistoryDataSerializer(data, many=True)
            return Response(data=serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        userhistory_data = JSONParser().parse(request)
        serializer = UserHistoryDataSerializer(data=userhistory_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserHistoryDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = UserHistory.objects.get(payment_id=slug)
            serializer = UserHistoryDataSerializer(hdata)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        try:
            hdata = UserHistory.objects.get(payment_id=slug)
            serializer = UserHistoryDataSerializer(hdata, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        try:
            hdata = UserHistory.objects.get(payment_id=slug)
            delresult = hdata.delete()
            data = {'message': 'error during deletion'}
            if delresult[0] == 1:
                data = {'message': 'successfully deleted'}
            return Response(data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserHistoryDetailUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            hdata = UserHistory.objects.filter(user_email=slug)
            serializer = UserHistoryDataSerializer(hdata, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


class SkyScannerListPlaces(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        query = request.GET.get('query', '')
        country = request.GET.get('country', '')
        currency = request.GET.get('currency', '')
        locale = request.GET.get('locale', '')
        url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/{country}/{currency}/{locale}/"

        querystring = {"query": f"{query}"}

        headers = {
            'x-rapidapi-key': "5c5035c1e7msh72f101263df16acp1caccdjsna75f7e1a26e5",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return Response(data=response.json())


class SkyScannerBrowseQuotes(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        country = request.GET.get('country', '')
        currency = request.GET.get('currency', '')
        locale = request.GET.get('locale', '')
        originplace = request.GET.get('originplace', '')
        destinationplace = request.GET.get('destinationplace', '')
        outboundpartialdate = request.GET.get('outboundpartialdate', '')

        url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/{country}/{currency}/{locale}/{originplace}/{destinationplace}/{outboundpartialdate}'

        querystring = {"inboundpartialdate": f"{outboundpartialdate}"}

        headers = {
            'x-rapidapi-key': "5c5035c1e7msh72f101263df16acp1caccdjsna75f7e1a26e5",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return Response(data=response.json())


class SkyScannerBrowseRoutes(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        country = request.GET.get('country', '')
        currency = request.GET.get('currency', '')
        locale = request.GET.get('locale', '')
        originplace = request.GET.get('originplace', '')
        destinationplace = request.GET.get('destinationplace', '')
        outboundpartialdate = request.GET.get('outboundpartialdate', '')

        url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/{country}/{currency}/{locale}/{originplace}/{destinationplace}/{outboundpartialdate}"

        querystring = {"inboundpartialdate": f"{outboundpartialdate}"}

        headers = {
            'x-rapidapi-key': "5c5035c1e7msh72f101263df16acp1caccdjsna75f7e1a26e5",
            'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return Response(data=response.json())
