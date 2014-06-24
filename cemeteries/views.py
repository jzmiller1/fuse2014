import datetime
from django.views import generic
from .models import Cemetery, Marker, Person, Symbology, MarkerImage, WWDC
from django.db.models import Q


def get_rel_referer(referer):
    back = "/" + "/".join(referer.split('/')[3:])
    return back


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


class MarkerDetailView(generic.TemplateView):
    template_name = "cemeteries/markers_detail.html"

    def get_context_data(self, **kwargs):
        """ Resize image.

        Resizes an to specified height while keeping the images aspect ratio. Used in the Marker Detail template if image
        exists.
        """
        context = super(MarkerDetailView, self).get_context_data(**kwargs)
        image = MarkerImage.objects.filter(markerid=kwargs['pk']).first()
        if image is not None:
            h_ratio = image.image.height / 800.0
            w_ratio = image.image.width / 700.0
            image.height = image.image.height / max(h_ratio, w_ratio)
            image.width = image.image.width / max(h_ratio, w_ratio)
            context['image'] = image
        marker = Marker.objects.filter(markerid=kwargs['pk']).first()
        people = Person.objects.filter(markerid=kwargs['pk'])
        context['marker'] = marker
        context['people'] = people
        refer = self.request.META.get('HTTP_REFERER')
        if refer is not None:
            context['back'] = get_rel_referer(refer)
        return context


class PersonListView(generic.ListView):
    model = Person
    template_name = "cemeteries/person_simple.html"


class PersonDetailView(generic.TemplateView):
    template_name = "cemeteries/person_detail.html"

    def get_context_data(self, **kwargs):
        """ Resize image.

        Resizes an to specified height while keeping the images aspect ratio. Used in the Person Detail template if image
        exists.
        """
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        person = Person.objects.filter(pk=kwargs['pk']).first()
        image = MarkerImage.objects.filter(markerid=person.markerid.pk).first()
        if image is not None:
            h_ratio = image.image.height / 800.0
            w_ratio = image.image.width / 700.0
            image.height = image.image.height / max(h_ratio, w_ratio)
            image.width = image.image.width / max(h_ratio, w_ratio)
            context['image'] = image
        refer = self.request.META.get('HTTP_REFERER')
        if refer is not None:
            context['back'] = get_rel_referer(refer)
        context['person'] = person
        card = WWDC.objects.filter(person=person).first()
        context['wwdc'] = card
        return context


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


class MarkerMapView(generic.TemplateView):
    template_name = "cemeteries/marker_map.html"


class PersonMapView(generic.TemplateView):
    template_name= "cemeteries/person_map.html"


class SymbolMapView(generic.TemplateView):
    template_name = "cemeteries/symbol_map.html"

    def get_context_data(self, **kwargs):
        context = super(SymbolMapView, self).get_context_data(**kwargs)
        symbol = Symbology.objects.filter(pk=kwargs['pk']).first()
        context['markers'] = "/api/v1/markers?markerid=" + ",".join([str(marker.markerid) for marker in symbol.markers.all()])
        context['symbol'] = symbol.symbology
        return context


class WWDCView(generic.TemplateView):
    template_name = "cemeteries/wwdc.html"

    def get_context_data(self, **kwargs):
        context = super(WWDCView, self).get_context_data(**kwargs)

        def get_eligible(draft, registrations):
            eligible = Person.objects.filter(gender='Male')
            eligible = eligible.exclude(a_birth__gt=draft[0].isoformat().split('T')[0])
            eligible = eligible.exclude(a_birth__lt=draft[1].isoformat().split('T')[0])
            eligible = eligible.exclude(a_death__lt=draft[2].isoformat().split('T')[0])
            for registration in registrations:
                eligible = eligible.exclude(id__in=registration.values('pk'))
            for registrant in eligible:
                card = WWDC.objects.filter(person=registrant)
                registrant.wwdc = card.first()
            return eligible

        first_registration = (datetime.datetime(1896, 6, 5), datetime.datetime(1886, 6, 5), datetime.datetime(1917, 6, 5))
        second_registration = (datetime.datetime(1897, 6, 6), datetime.datetime(1896, 6, 6), datetime.datetime(1918, 6, 5))
        supplemental_registration = (datetime.datetime(1897, 8, 24), datetime.datetime(1897, 6, 6), datetime.datetime(1918, 6, 6))
        third_registration = (datetime.datetime(1900, 9, 12), datetime.datetime(1873, 9, 12), datetime.datetime(1918, 9, 12))
        registrations = [first_registration, second_registration, supplemental_registration, third_registration]
        registration_data = []

        for registration in registrations:
            registration_data.append(get_eligible(registration, registration_data))

        context['registrations'] = registration_data
        return context


class WWDCMapView(generic.TemplateView):
    template_name = "cemeteries/WWDC_map.html"

    def get_context_data(self, **kwargs):
        context = super(WWDCMapView, self).get_context_data(**kwargs)
        people = [str(card.person.pk) for card in WWDC.objects.all()]
        context['people'] = "/api/v1/people?id=" + ",".join(people)
        return context