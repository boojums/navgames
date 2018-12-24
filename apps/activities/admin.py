from django.contrib import admin
from cms.admin.placeholderadmin import FrontendEditableAdminMixin, \
    PlaceholderAdminMixin

from .models import Activity, Lesson


#class ActivityAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
#    frontend_editable_fields = ("description",)
    #inlines = [
    #    CourseInline,
    #]


admin.site.register(Activity)
#admin.site.register(Lesson)
