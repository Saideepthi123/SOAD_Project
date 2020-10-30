from django.contrib import admin
from Tourism.models import (Booking, Payment, UserHistory, )


admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(UserHistory)
