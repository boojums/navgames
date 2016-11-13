from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from events.models import Event


@toolbar_pool.register
class EventToolbar(CMSToolbar):
    supported_apps = (
        'events',
    )
    watch_models = [Event, ]

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('events-app', _('Events'))

        menu.add_sideframe_item(
            name=_('Event list'),
            url=admin_reverse('events_event_changelist'),
        )

        menu.add_modal_item(
            name=_('Add new event'),
            url=admin_reverse('events_event_add'),
        )

        menu.add_sideframe_item(
            name=_('Locations list'),
            url=admin_reverse('events_location_changelist'),
        )

        menu.add_sideframe_item(
            name=_('Series list'),
            url=admin_reverse('events_series_changelist'),
        )
