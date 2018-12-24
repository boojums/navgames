''' Support for CMS app.'''
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ActivitiesApphook(CMSApp):
    ''' Main unit of activity as an app.'''
    app_name = "activities"
    name = _("Activities")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["activities.urls"]

apphook_pool.register(ActivitiesApphook)
