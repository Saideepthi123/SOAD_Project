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
from django.conf import settings
import stripe


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


def sky_scanner_list_places(request, query, country, currency, locale):
    url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/{country}/{currency}/{locale}/"

    querystring = {"query": f"{query}"}

    headers = {
        'x-rapidapi-key': settings.SKYSCANNER_KEY,
        'x-rapidapi-host': settings.SKYSCANNER_HOST
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    places = data['Places']

    place_ids = []
    for i in range(len(places)):
        place_ids.append(places[i]['PlaceId'])

    return place_ids


class SkyScannerSearchFlights(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        country = request.data['country']
        currency = request.data['currency']
        locale = request.data['locale']
        originplace = request.data['originplace']
        destinationplace = request.data['destinationplace']
        outboundpartialdate = request.data['outboundpartialdate']
        originplace_ids = []
        destinationplace_ids = []
        search_flights = []

        originplace = sky_scanner_list_places(request, originplace, country, currency, locale)
        destinationplace = sky_scanner_list_places(request, destinationplace, country, currency, locale)
        for i in range(len(originplace)):
            originplace_ids.append(originplace[i])
            originplace_ids = list(set(originplace_ids))

        for j in range(len(destinationplace)):
            destinationplace_ids.append(destinationplace[j])
            destinationplace_ids = list(set(destinationplace_ids))
        for i in range(len(originplace_ids)):
            for j in range(len(destinationplace_ids)):
                url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/{country}/{currency}/{locale}/{originplace_ids[i]}/{destinationplace[j]}/{outboundpartialdate}'
                querystring = {"inboundpartialdate": f"{outboundpartialdate}"}
                headers = {
                    'x-rapidapi-key': settings.SKYSCANNER_KEY,
                    'x-rapidapi-host': settings.SKYSCANNER_HOST
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                response = response.json()
                quotes = response['Quotes']
                carriers = response['Carriers']
                flights_details = {}
                for k in range(len(quotes)):
                    if not quotes[k] and carriers[k]:
                        continue
                    else:
                        flights_details['CarrierName'] = carriers[k]['Name']
                        flights_details['MinPrice'] = quotes[k]['MinPrice']
                        flights_details['Direct'] = quotes[k]['Direct']
                        flights_details['DepartureDate'] = quotes[k]['OutboundLeg']['DepartureDate']
                search_flights.append(flights_details) if flights_details else None
        return Response(data=search_flights)


class SkyScannerFlightRoutes(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        country = request.data['country']
        currency = request.data['currency']
        locale = request.data['locale']
        originplace = request.data['originplace']
        destinationplace = request.data['destinationplace']
        outboundpartialdate = request.data['outboundpartialdate']
        originplace_ids = []
        destinationplace_ids = []
        flight_routes = []

        originplace = sky_scanner_list_places(request, originplace, country, currency, locale)
        destinationplace = sky_scanner_list_places(request, destinationplace, country, currency, locale)

        for i in range(len(originplace)):
            for j in range(len(destinationplace)):
                originplace_ids.append(originplace[i])
                destinationplace_ids.append(destinationplace[j])
                url = f'https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/{country}/{currency}/{locale}/{originplace_ids[i]}/{destinationplace[j]}/{outboundpartialdate}'
                querystring = {"inboundpartialdate": f"{outboundpartialdate}"}
                headers = {
                    'x-rapidapi-key': settings.SKYSCANNER_KEY,
                    'x-rapidapi-host': settings.SKYSCANNER_HOST
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                flight_routes.append(response.json())
        return Response(data=flight_routes)