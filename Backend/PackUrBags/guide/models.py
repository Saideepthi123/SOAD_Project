from djongo import models
from datetime import datetime

# Create your models here.
class Place(models.Model):
    place = models.CharField(max_length=50)

class GuideData(models.Model):
    guide_id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    place      = models.ManyToManyField(Place)
    profile_pic = models.ImageField(default='no_image.png', upload_to='guide_profile_pics/')
    dob = models.DateField(default=datetime.today)
    address = models.TextField()

    def __str__(self):
        return self.email