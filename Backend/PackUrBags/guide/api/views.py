from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from guide.models import GuideData
from monuments.models import Monument, City
from Tourism.models import Booking, Payment
from authentication.models import UserData
from .serializers import GuideDataSerializer, SearchGuideSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from datetime import datetime, date
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.shortcuts import render, redirect
from PackUrBags import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
key = settings.STRIPE_PUBLIC_KEY
=======
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from datetime import datetime
from rest_framework.authtoken.models import Token 
from authentication.models import UserData 
from authentication.api.utils import Util
from django.http import JsonResponse
>>>>>>> 7a19abb95a3ad893e9a321f5007323e9e5a21e4d


class SearchGuides(generics.GenericAPIView):
    serializer_class = SearchGuideSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data)
        data = serializer.data
        try:
            city = City.objects.get(city_name=data['city'])
        except ObjectDoesNotExist:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)
        monuments = city.monuments.all()
        self.queryset = GuideData.objects.filter(place__in=monuments)
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
        start_date = date(start_date.year, start_date.month, start_date.day)
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
        end_date = date(end_date.year, end_date.month, end_date.day)
        no_of_days = end_date - start_date
        available_guides = []
        for i in range(len(self.queryset)):
            guide = self.queryset[i]
            if GuideData.is_available(guide, start_date) is True:
                available_guides.append(guide)
        serializer = GuideDataSerializer(available_guides, many=True)
        data = serializer.data
        for i in range(len(data)):
            data[i]['no_of_days'] = no_of_days.days
        return Response(data)


class BookingGuide(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, guide_id, user_id, no_of_days):
        guide = GuideData.objects.get(guide_id=guide_id)
        cost = GuideData.get_cost(guide, no_of_days)
        start_date = request.GET.get('start_date', '')
        end_date = request.GET.get('end_date', '')
        serializer = GuideDataSerializer(guide)
        data = serializer.data
        data['cost'] = cost * 100
        data['user_id'] = user_id
        return render(request, 'payment_page.html', {'cost': cost, 'key': key, 'guide_id': guide_id,
                                                     'user_id': user_id, 'start_date': start_date, 'end_date': end_date})


@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        token = request.POST.get("stripeToken")
        cost = request.POST['cost']
        guide_id = request.POST['guide_id']
        user_id = request.POST['user_id']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        guide = GuideData.objects.get(guide_id=guide_id)
        user = UserData.objects.get(id=user_id)
        booking = Booking.objects.create(user_email=user, guide_email=guide).save()
        GuideData.objects.filter(guide_id=guide_id).update(last_booking_start_date=start_date, last_booking_end_date=end_date)
        payment = Payment.objects.create(booking_id=booking, user_email=user, guide_email=guide, mode_of_payment='1')
        try:
            charge = stripe.Charge.create(
                amount=cost,
                currency="inr",
                source=token,
                description="The product charged to the user"
            )
            payment.charge_id = charge.id
            payment.save()
            return redirect('home')
        except stripe.error.CardError as ce:
            return False, ce


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


class getToken(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        data = request.data
        pk = data['pk']
        user = UserData.objects.get(pk=pk)
        token, created = Token.objects.get_or_create(user=user)

        email_body = 'Hi ' + user.username + 'Your API KEY' + str(token)    
        message = {'email_body': email_body, 'email_subject': 'Token', 'to_email': (user.email,)}
        Util.send_email(message)

        return JsonResponse({"Token": str(token)})
        
class ExposeGuidesService(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        data = request.data
        token = data['token']
        if(token is None):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            try:
                data = GuideData.objects.all()
                print(data)
                serializer = GuideDataSerializer(data, many=True)
                return Response(data=serializer.data)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
