from djongo import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime


# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.username = username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserData(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    profile_pic = models.ImageField(default='no_image.png', upload_to='user_profile_pics/')
    dob = models.DateField(default=datetime.today)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class GuideData(models.Model):
    guide_id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    profile_pic = models.ImageField(default='no_image.png', upload_to='guide_profile_pics/')
    dob = models.DateField(default=datetime.today)
    address = models.TextField()

    def __str__(self):
        return self.email


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

    def __int__(self):
        return self.booking_id


class Monument(models.Model):
    monument_id = models.AutoField(primary_key=True)
    monument_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    basic_info = models.TextField()
    pin_code = models.CharField(max_length=6)

    def __str__(self):
        return self.monument_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)

    def __str__(self):
        return self.city_name


class MonumentInfo(models.Model):
    monument_info_id = models.AutoField(primary_key=True)
    monument_name = models.ForeignKey(Monument, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return f'{self.monument_name}\'s info'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="p_booking_id")
    user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="p_user_email")
    guide_email = models.ForeignKey(GuideData, on_delete=models.CASCADE, related_name="p_guide_email")
    mode_of_payment = models.CharField(max_length=20)
    timestamp = models.DateTimeField(verbose_name='Booked at ', auto_now=True)

    def get_user_data(self):
        user = UserData.objects.get(email=self.user_email)
        return user

    def get_booking_details(self):
        booking = Booking.objects.get(booking_id=self.booking_id)
        return booking

    def __int__(self):
        return self.payment_id


# class UserTravelHistory(models.Model):
#     modes = (
#         (1, 'Bus'),
#         (2, 'Flight'),
#         (3, 'Train'),
#         (4, 'Cab'),
#         (5, 'Ship')
#     )
#     user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="ut_user_email")
#     mode_of_travel = models.IntegerField(choices=modes, default=1)
#     travel_amount = models.IntegerField()
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return f'{self.user_email}\'s travel history'
#
#
# class UserFoodHistory(models.Model):
#     user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="uf_user_email")
#     restaurant = models.CharField(max_length=100)
#     food_amount = models.IntegerField()
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return f'{self.user_email}\'s food history'
#
#
# class UserStayHistory(models.Model):
#     user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="us_user_email")
#     lodge = models.CharField(max_length=100)
#     stay_amount = models.IntegerField()
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return f'{self.user_email}\'s stay history'
#
#
# class UserHistory(models.Model):
#     user_email = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name="u_user_email")
#     mode_of_payment = models.CharField(max_length=20)
#     timestamp = models.DateTimeField(verbose_name='Booked at ', auto_now=True)
#     travel_history = models.ForeignKey(UserTravelHistory, on_delete=models.CASCADE)
#     food_history = models.ForeignKey(UserFoodHistory, on_delete=models.CASCADE)
#     stay_history = models.ForeignKey(UserStayHistory, on_delete=models.CASCADE)
#     travel = UserTravelHistory.objects.filter(email=user_email)
#     food = UserFoodHistory.objects.filter(email=user_email)
#     stay = UserStayHistory.objects.filter(email=user_email)
#
#     def __str__(self):
#         return f'{self.user_email}\'s history'
