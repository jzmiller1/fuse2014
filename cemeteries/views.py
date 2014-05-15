from django.views import generic
from .models import Cemetery, Marker, Person, Symbology
from django.db.models import Q
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


class PeopleView(generic.TemplateView):
    template_name = "cemeteries/people_view.html"

    def get_context_data(self, **kwargs):
        context = super(PeopleView, self).get_context_data(**kwargs)
        groups = [['A', 'B ', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
                  ['M', 'N', 'O'], ['P', 'Q', 'R'], ['S', 'T', 'U'], ['V', 'W', 'X'],
                  ['Y', 'Z']]
        data = {}

        def group_people(letters):
            """ Using letters to locate matching letters in the database.

            The function group_people takes a list of letters as parameters and runs a query on the database. The the
            data is collected in a list and returned to a dictionary to be passed into the template.

            """
            key = " ".join(letters)
            qs = [Q(last_name__istartswith=letter) for letter in letters]
            final_q = None
            for q in qs:
                final_q = final_q | q if final_q else q
            p = Person.objects.filter(final_q)
            data[key] = p
        for g in groups:
            group_people(g)
        data = list(data.items())
        data.sort()
        context['groups'] = data
        return context


class SymbologyView(generic.ListView):
    model = Symbology
    template_name = "cemeteries/symbology.html"
