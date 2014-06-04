from django.conf.urls import patterns, include, url
from .views import MainView, CemeteryListView, CemeteryDetailView, MarkerListView,MarkerDetailView
from .views import PersonListView, PersonDetailView,AboutView, SymbologyView, PeopleView, MarkerMapView,PersonMapView, SymbolMapView
from .models import Cemetery, Marker, Person, Symbology
from django.contrib.auth.decorators import login_required
from djgeojson.views import GeoJSONLayerView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuse2014.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main$', MainView.as_view(), name='main'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^cemeteries/$', login_required(CemeteryListView.as_view(model=Cemetery)), name='cem_lview'),
    url(r'^cemeteries/(?P<pk>\d+)/$', login_required(CemeteryDetailView.as_view()), name='cem_dview'),
    url(r'^marker/$', login_required(MarkerListView.as_view(model=Marker)), name='marker_lview'),
    url(r'^marker/(?P<pk>\d+)/$', login_required(MarkerDetailView.as_view()),name='marker_dview'),
    url(r'^person/$', login_required(PersonListView.as_view(model=Person)), name='person_lview'),
    url(r'^person/(?P<pk>\d+)/$', login_required(PersonDetailView.as_view()), name='person_dview'),
    url(r'^people_search/$', login_required(PeopleView.as_view()), name='people_view'),
    url(r'^symbology/$', login_required(SymbologyView.as_view(model=Symbology)), name='symbology'),
    url(r'^map_marker/$', login_required(MarkerMapView.as_view()), name='markermap'),
    url(r'^map_person/$', login_required(PersonMapView.as_view()), name='personmap'),
    url(r'^symbolmap/(?P<pk>\d+)/$', login_required(SymbolMapView.as_view()), name='symbolmap'),
)
