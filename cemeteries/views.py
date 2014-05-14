from django.views import generic
from .models import Cemetery, Marker, Person
# Create your views here.


class MainView(generic.TemplateView):
    template_name = "cemeteries/mainpage.html"


class CemeteryListView(generic.ListView):
    model = Cemetery
    template_name = "cemeteries/cemeteries_simple.html"


class CemeteryDetailView(generic.DetailView):
    model = Cemetery
    template_name = "cemeteries/cemeteries_detail.html"


class MarkerListView(generic.ListView):
    model = Marker
    template_name = "cemeteries/markers_simple.html"


class MarkerDetailView(generic.DetailView):
    model = Marker
    template_name = "cemeteries/markers_detail.html"


class PersonListView(generic.ListView):
    model = Person
    template_name = "cemeteries/person_simple.html"


class PersonDetailView(generic.DetailView):
    model = Person
    template_name = "cemeteries/person_detail.html"


class AboutView(generic.TemplateView):
    template_name = "cemeteries/about.html"
