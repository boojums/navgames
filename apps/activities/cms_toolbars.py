''' Support for a CMS toolbar for the Activity app'''
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from .models import Activity


@toolbar_pool.register
class ActivityToolbar(CMSToolbar):
    ''' Acitivty toolbar'''
    supported_apps = (
        'activities',
    )
    watch_models = [Activity, ]

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('activities-app', _('Activities'))

        menu.add_sideframe_item(
            name=_('Activity list'),
            url=admin_reverse('activities_activity_changelist'),
        )

        menu.add_modal_item(
            name=_('Add new activity'),
            url=admin_reverse('activities_activity_add'),
        )

        # menu.add_sideframe_item(
        #     name=_('Locations list'),
        #     url=admin_reverse('events_location_changelist'),
        # )

        # menu.add_sideframe_item(
        #     name=_('Series list'),
        #     url=admin_reverse('events_series_changelist'),
        # )
