from django.contrib .syndication.views import Feed
from django.core.urlresolvers import reverse

from .models import Event


class LatestEventsFeed(Feed):
    title = "Navigation Games events"
    link = "/events/upcoming/"
    description = "Upcoming events hosted by Navigation Games"

    def items(self):
        return Event.future_events.all().order_by('start_date')

    def item_title(self, item):
        return str(item)

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('events:event-detail', kwargs={'slug': item.slug})
