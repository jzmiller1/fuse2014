from django.conf.urls import patterns, include, url
from .views import MainView, CemeteryListView, CemeteryDetailView, MarkerListView,MarkerDetailView
from .views import PersonListView, PersonDetailView,AboutView
from .models import Cemetery, Marker, Person




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuse2014.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main$', MainView.as_view(), name='main'),
    url(r'^cemeteries/$', CemeteryListView.as_view(model=Cemetery), name='cem_lview'),
    url(r'^cemeteries/(?P<pk>\d+)/$', CemeteryDetailView.as_view(), name='cem_dview'),
    url(r'^marker/$', MarkerListView.as_view(model=Marker), name='marker_lview'),
    url(r'^marker/(?P<pk>\d+)/$', MarkerDetailView.as_view(),name='marker_dview'),
    url(r'^person/$', PersonListView.as_view(model=Person), name='person_lview'),
    url(r'^person/(?P<pk>\d+)/$', PersonDetailView.as_view(), name='person_dview'),
    url(r'^about/$', AboutView.as_view(), name='about'),
)
