from django.contrib import admin
from tourism.models import (Booking, Monument, City, GuideData, MonumentInfo, Payment, UserHistory, )


admin.site.register(Booking)
admin.site.register(Monument)
admin.site.register(City)
admin.site.register(GuideData)
admin.site.register(MonumentInfo)
admin.site.register(Payment)
admin.site.register(UserHistory)
