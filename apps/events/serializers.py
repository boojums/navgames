from rest_framework import serializers
from .models import Event


class LocationListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class EventSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="events:event-detail")
    location = LocationListingField(many=False, read_only=True)

    class Meta:
        model = Event
        fields = ('url', 'name', 'location', 'start_date',
                  'description', 'public')
