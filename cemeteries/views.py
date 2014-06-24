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
        draft1 = Person.objects.filter(gender='Male').exclude(a_birth__gt=datetime.datetime(1896, 6, 5).isoformat().split('T')[0])
        draft1 = draft1.exclude(a_birth__lt=datetime.datetime(1886, 6, 5).isoformat().split('T')[0])
        draft1 = draft1.exclude(a_death__lt=datetime.datetime(1917, 6, 5).isoformat().split('T')[0])
        for draftee in draft1:
            card = WWDC.objects.filter(person=draftee)
            draftee.wwdc = card.first()

        draft2 = Person.objects.filter(gender='Male').exclude(a_birth__gt=datetime.datetime(1897, 6, 6).isoformat().split('T')[0])
        draft2 = draft2.exclude(a_birth__lt=datetime.datetime(1896, 6, 6).isoformat().split('T')[0])
        draft2 = draft2.exclude(a_death__lt=datetime.datetime(1918, 6, 5).isoformat().split('T')[0])
        draft2 = draft2.exclude(id__in=draft1.values('pk'))
        for draftee in draft2:
            card = WWDC.objects.filter(person=draftee)
            draftee.wwdc = card.first()

        draft3 = Person.objects.filter(gender='Male').exclude(a_birth__gt=datetime.datetime(1897, 8, 24).isoformat().split('T')[0])
        draft3 = draft3.exclude(a_birth__lt=datetime.datetime(1897, 6, 6).isoformat().split('T')[0])
        draft3 = draft3.exclude(a_death__lt=datetime.datetime(1918, 6, 6).isoformat().split('T')[0])
        draft3 = draft3.exclude(id__in=draft1.values('pk'))
        draft3 = draft3.exclude(id__in=draft2.values('pk'))
        for draftee in draft3:
            card = WWDC.objects.filter(person=draftee)
            draftee.wwdc = card.first()

        draft4 = Person.objects.filter(gender='Male').exclude(a_birth__gt=datetime.datetime(1900, 9, 12).isoformat().split('T')[0])
        draft4 = draft4.exclude(a_birth__lt=datetime.datetime(1873, 9, 12).isoformat().split('T')[0])
        draft4 = draft4.exclude(a_death__lt=datetime.datetime(1918, 9, 12).isoformat().split('T')[0])
        draft4 = draft4.exclude(id__in=draft1.values('pk'))
        draft4 = draft4.exclude(id__in=draft2.values('pk'))
        draft4 = draft4.exclude(id__in=draft3.values('pk'))
        for draftee in draft4:
            card = WWDC.objects.filter(person=draftee)
            draftee.wwdc = card.first()

        context['draft1'] = draft1
        context['draft2'] = draft2
        context['draft3'] = draft3
        context['draft4'] = draft4
        return context


class WWDCMapView(generic.TemplateView):
    template_name = "cemeteries/WWDC_map.html"

    def get_context_data(self, **kwargs):
        context = super(WWDCMapView, self).get_context_data(**kwargs)
        people = [str(card.person.pk) for card in WWDC.objects.all()]
        context['people'] = "/api/v1/people?id=" + ",".join(people)
        return context