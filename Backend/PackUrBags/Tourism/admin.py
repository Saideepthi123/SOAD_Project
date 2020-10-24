from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Tourism.models import UserData, Booking, Monument, City, GuideData, MonumentInfo, Payment


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', 'is_staff',)
    search_fields = ('email', 'username',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserData, AccountAdmin)
admin.site.register(Booking)
admin.site.register(Monument)
admin.site.register(City)
admin.site.register(GuideData)
admin.site.register(MonumentInfo)
admin.site.register(Payment)
