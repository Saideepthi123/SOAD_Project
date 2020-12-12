from djongo import models
from datetime import datetime
from monuments.models import Monument


class GuideData(models.Model):
    guide_id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    place = models.ManyToManyField(Monument)
    profile_pic = models.ImageField(default='no_image.png', upload_to='guide_profile_pics/')
    dob = models.DateField(default=datetime.today)
    address = models.TextField()
    last_booking_start_date = models.DateField(default=datetime.today, blank=True)
    last_booking_end_date = models.DateField(default=datetime.today, blank=True)

    def is_available(self, start_date):
        return self.last_booking_end_date < start_date

    def get_cost(self, no_of_days):
        starting_cost = 1000
        cost = starting_cost + (1500 * no_of_days)
        return cost

    def __str__(self):
        return self.email
