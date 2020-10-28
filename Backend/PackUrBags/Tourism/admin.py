from django.contrib import admin
from tourism.models import (Booking, Payment, UserHistory, )


admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(UserHistory)
