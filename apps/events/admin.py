from django.contrib import admin
from django.forms import BaseInlineFormSet
from cms.admin.placeholderadmin import FrontendEditableAdminMixin, \
                                       PlaceholderAdminMixin

from .models import Location, Event, Series, Result, Course, Club


class CourseInline(admin.TabularInline):
    model = Course


class EventAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    frontend_editable_fields = ("description",)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        CourseInline,
    ]


class LocationAdmin(FrontendEditableAdminMixin, PlaceholderAdminMixin,
                    admin.ModelAdmin):
    frontend_editable_fields = ("description",)


class ResultInline(admin.TabularInline):
    model = Result


class CourseAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
    inlines = [
        ResultInline
    ]

admin.site.register(Location)
admin.site.register(Event, EventAdmin)
admin.site.register(Series)
admin.site.register(Result)
admin.site.register(Course, CourseAdmin)
admin.site.register(Club)
