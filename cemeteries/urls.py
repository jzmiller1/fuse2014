from django.conf.urls import patterns, include, url
from .views import MainView, CemeteryListView, CemeteryDetailView, MarkerListView,MarkerDetailView
from .views import PersonListView, PersonDetailView,AboutView, SymbologyView, PeopleView, MarkerMapView,PersonMapView, SymbolMapView
from .models import Cemetery, Marker, Person, Symbology
#from django.contrib.auth.decorators import login_required



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuse2014.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', MainView.as_view(), name='main'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^cemeteries/$', CemeteryListView.as_view(model=Cemetery), name='cem_lview'),
    url(r'^cemeteries/(?P<pk>\d+)/$', CemeteryDetailView.as_view(), name='cem_dview'),
    url(r'^marker/$', MarkerListView.as_view(model=Marker), name='marker_lview'),
    url(r'^marker/(?P<pk>\d+)/$', MarkerDetailView.as_view(), name='marker_dview'),
    url(r'^person/$', PersonListView.as_view(model=Person), name='person_lview'),
    url(r'^person/(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person_dview'),
    url(r'^people_search/$', PeopleView.as_view(), name='people_view'),
    url(r'^symbology/$', SymbologyView.as_view(model=Symbology), name='symbology'),
    url(r'^map_marker/$', MarkerMapView.as_view(), name='markermap'),
    url(r'^map_person/$', PersonMapView.as_view(), name='personmap'),
    url(r'^symbolmap/(?P<pk>\d+)/$', SymbolMapView.as_view(), name='symbolmap'),
)
