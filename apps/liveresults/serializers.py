from rest_framework import serializers

from .models import Event, Race


class EventSerializer(serializers.HyperlinkedModelSerializer):
    races = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='liveresults:race-detail',
        many=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'start_date', 'end_date', 'races')


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(read_only=True, view_name='liveresults:event-detail')

    class Meta:
        model = Race
        fields = ('id', 'name', 'date', 'startlist', 'resultslist', 'event')
