from django.contrib import admin

from lights.models import LightSample


class LightSampleAdmin(admin.ModelAdmin):
    list_display = ('state', 'created_date')


admin.site.register(LightSample, LightSampleAdmin)
