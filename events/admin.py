from django.contrib import admin

from .models import Location, Event, Series


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Location)
admin.site.register(Event, EventAdmin)
admin.site.register(Series)
