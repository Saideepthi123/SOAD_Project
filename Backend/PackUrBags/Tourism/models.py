from djongo import models
from authentication.models import UserData
from guide.models import GuideData
# Create your models here.


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="b_user_email")
    guide_email = models.ForeignKey(GuideData, on_delete=models.CASCADE, related_name="b_guide_email")
    timestamp = models.DateTimeField(verbose_name='Booked at ', auto_now=True)

    def get_user_data(self):
        user = UserData.objects.get(email=self.user_email)
        return user

    def get_guide_data(self):
        guide = GuideData.objects.get(email=self.guide_email)
        return guide

    def __str__(self):
        return str(self.booking_id)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="p_booking_id")
    user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="p_user_email")
    guide_email = models.ForeignKey(GuideData, on_delete=models.CASCADE, related_name="p_guide_email")
    payment_modes = (
        ('1', 'Debit/Credit card'),
        ('2', 'UPI'),
        ('3', 'Cash'),
        ('4', 'Net banking'),
    )
    mode_of_payment = models.CharField(choices=payment_modes, default='2', max_length=1)
    timestamp = models.DateTimeField(verbose_name='Booked at ', auto_now=True)

    def get_user_data(self):
        user = UserData.objects.get(email=self.user_email)
        return user

    def get_booking_details(self):
        booking = Booking.objects.get(booking_id=self.booking_id)
        return booking

    def __str__(self):
        return str(self.payment_id)


class UserHistory(models.Model):
    user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="u_user_email")
    payment_modes = (
        ('1', 'Debit/Credit card'),
        ('2', 'UPI'),
        ('3', 'Cash'),
        ('4', 'Net banking'),
    )
    mode_of_payment = models.CharField(choices=payment_modes, default='2', max_length=1)
    timestamp = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="u_timestamp")
    modes = (
        (1, 'Bus'),
        (2, 'Flight'),
        (3, 'Train'),
        (4, 'Cab'),
        (5, 'Ship'),
    )
    mode_of_travel = models.IntegerField(choices=modes, default=1)
    travel_amount = models.IntegerField()
    restaurant = models.CharField(max_length=100)
    food_amount = models.IntegerField()
    lodge = models.CharField(max_length=100)
    stay_amount = models.IntegerField()

    def __str__(self):
        return f'{self.user_email}\'s history {self.pk}'
