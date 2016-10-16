from django.contrib import admin
from cms.admin.placeholderadmin import FrontendEditableAdminMixin, \
                                       PlaceholderAdminMixin

from .models import Location, Event, Series, UserProfile


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class LocationAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                    admin.ModelAdmin):
    frontend_editable_fields = ("description",)


admin.site.register(Location)
admin.site.register(Event, EventAdmin)
admin.site.register(Series)
admin.site.register(UserProfile)
