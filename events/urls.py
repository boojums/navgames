from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.EventList.as_view(), name='event-list'),
    url(r'detail/(?P<slug>[\w\-]+)/$', views.EventDetail.as_view(),
        name='event-detail'),
    url(r'add/$', views.EventCreate.as_view(), name='event-add'),
    url(r'delete/(?P<slug>[\w\-]+)/$', views.EventDelete.as_view(),
        name='event-delete'),
]
