import datetime

from django.test import TestCase
from django.utils import timezone

from events.models import Event, Location, Series


class EventMethodTests(TestCase):

    def setUp(self):
        now = timezone.now()
        description = "this is a description"
        loc = Location.objects.create(name="SuperSprint", city="Cambridge")
        self.past_event = Event.objects.create(
            start_date=now-datetime.timedelta(days=5),
            location=loc,
            description=description,
            uses_epunch=True,
            public=True)

    def test_is_future_with_future_event(self):
        self.assertIs(self.past_event.is_past(), True)

    def test_is_future_with_past_event(self):
        pass

    def test_is_past_with_future_event(self):
        pass

    def test_is_past_with_past_event(self):
        pass

    def test_is_past_with_today_event(self):
        pass

    def test_is_future_with_today_event(self):
        pass