from django.contrib import admin
from monuments.models import Monument, City, MonumentInfo

# Register your models here.
admin.site.register(Monument)
admin.site.register(MonumentInfo)
admin.site.register(City)
