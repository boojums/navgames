from django.conf.urls import url
from .feeds import LatestEventsFeed, EventsICal

from . import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.EventList.as_view(), name='event-list'),
    url(r'detail/(?P<slug>[\w\-]+)/$', views.EventDetail.as_view(),
        name='event-detail'),
    url(r'add/$', views.EventCreate.as_view(), name='event-add'),
    url(r'delete/(?P<slug>[\w\-]+)/$', views.EventDelete.as_view(),
        name='event-delete'),

    url(r'location/(?P<slug>[\w\-]+)/$', views.LocationDetail.as_view(),
        name='location-detail'),
    url(r'location/list/', views.LocationList.as_view(), name='location-list'),

    url(r'feed/$', LatestEventsFeed()),
    url(r'ical/$', EventsICal())
]
