from django.db import models

# Create your models here.

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)

    def __str__(self):
        return self.city_name



class Monument(models.Model):
    monument_id = models.AutoField(primary_key=True)
    monument_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    basic_info = models.TextField()
    pin_code = models.CharField(max_length=6)
    city = models.ManyToManyField(City)

    def __str__(self):
        return self.monument_name





class MonumentInfo(models.Model):
    monument_info_id = models.AutoField(primary_key=True)
    monument_name = models.ForeignKey(Monument, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return f'{self.monument_name}\'s info'