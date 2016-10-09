from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EventList.as_view(), name='event-list'),
    url(r'events/(?P<slug>[\w\-]+)/$', views.EventDetail.as_view(),
        name='event-detail'),
    url(r'add/$', views.EventCreate.as_view(), name='event-add')
]
