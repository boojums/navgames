from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import EventPluginModel, EventListPluginModel, Event
from django.utils.translation import ugettext as _
from django.utils import timezone


@plugin_pool.register_plugin
class EventPluginPublisher(CMSPluginBase):
    model = EventPluginModel  # model where plugin data are saved
    module = _("Events")
    name = _("Event Detail")  # name of the plugin in the interface
    render_template = "events/detail.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class EventListPluginPublisher(CMSPluginBase):
    model = EventListPluginModel  # model where plugin data are saved
    module = _("Events")
    name = _("Events List")  # name of the plugin in the interface
    render_template = "events/plugins/event_list.html"

    def render(self, context, instance, placeholder):
        events = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date')[:instance.n_events]
        context.update({'instance': instance,
                        'latest_events_list': events})
        return context

# TODO: series publisher?

#plugin_pool.register_plugin(EventPluginPublisher)  # register the plugin
#plugin_pool.register_plugin(EventListPluginPublisher)  # register the plugin
