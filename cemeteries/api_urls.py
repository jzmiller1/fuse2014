from django.conf.urls import patterns, include, url
from cemeteries.json_views import PeopleCollection, PersonCollection, MarkerCollection, MarkersCollection

urlpatterns = patterns('',
    # Examples:
    url(r'^people$', PeopleCollection.as_view(), name='people_collection'),
    url(r'^person/(?P<pk>[0-9]+)$', PersonCollection.as_view(), name='person_collection'),
    url(r'^markers$', MarkersCollection.as_view(), name='markers_collection'),
    url(r'^marker/(?P<pk>[0-9]+)$', MarkerCollection.as_view(), name='marker_collection'),
)
