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
    name = _("Event List")  # name of the plugin in the interface
    render_template = "events/plugins/event_list.html"

    def render(self, context, instance, placeholder):
        if instance.past_events and instance.future_events:
            events = Event.objects.all()
        elif instance.past_events:
            events = Event.past_events.all()
        else:
            events = Event.future_events.all()

        if instance.only_public:
            events = events.filter(public=True)

        if instance.series:
            events = events.filter(series=instance.series)

        event_list = events.order_by('start_date')[:instance.num_events]
        context.update({'instance': instance,
                        'event_list': event_list})
        return context
