from django.db import models

# Create your models here.


class Monument(models.Model):
    monument_id = models.AutoField(primary_key=True)
    monument_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    basic_info = models.TextField()
    pin_code = models.CharField(max_length=6)
    imageURL = models.TextField(
        default="https://img.freepik.com/free-vector/cityscape-cartoon-background-panorama-modern-city-with-high-skyscrapers-park-downtown_1441-1982.jpg?size=626&ext=jpg")
    # in_city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.monument_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)
    city_info = models.TextField(default="city info")
    imageURL = models.TextField(
        default="https://img.freepik.com/free-vector/cityscape-cartoon-background-panorama-modern-city-with-high-skyscrapers-park-downtown_1441-1982.jpg?size=626&ext=jpg")
    monuments = models.ManyToManyField(Monument)

    def __str__(self):
        return self.city_name


class MonumentInfo(models.Model):
    monument_info_id = models.AutoField(primary_key=True)
    monument_name = models.ForeignKey(Monument, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    info = models.TextField()
    imageURL = models.TextField(
        default="https://img.freepik.com/free-vector/cityscape-cartoon-background-panorama-modern-city-with-high-skyscrapers-park-downtown_1441-1982.jpg?size=626&ext=jpg")

    def __str__(self):
        return f'{self.monument_name}\'s info'
