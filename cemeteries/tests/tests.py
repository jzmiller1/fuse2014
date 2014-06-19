from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from cemeteries.views import MainView, CemeteryListView, CemeteryDetailView, MarkerListView, MarkerDetailView
from cemeteries.views import PersonListView, PersonDetailView, AboutView, SymbologyView, PeopleView, MarkerMapView, PersonMapView
from cemeteries.views import SymbolMapView, WWDCView, WWDCMapView
from cemeteries.json_views import PeopleCollection, PersonCollection, MarkersCollection, MarkerCollection
from cemeteries import models


class MarkerTestCase(TestCase):
    def setUp(self):
        pass
        # Tests run against initial_data.json fixture data so creating test data within the test is not needed.
        # models.Cemetery.objects.create(name="test_cem", description="test")
        # models.Marker.objects.create(cemetery=models.Cemetery.objects.get(name="test_cem"),
        #                              markerid=6027,
        #                              condition="Aged",
        #                              readable=True,
        #                              epitaph="RIP",
        #                              family_name="Tester",
        #                             )

    def test_marker_string(self):
        """Verifying __str__ returns with proper formatting."""
        marker = models.Marker.objects.get(markerid=6027)
        self.assertEqual(marker.__str__(), "Markerid: 6027 - Timberidge Cemetery")

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        marker = models.Marker.objects.get(markerid=6027)
        self.assertEqual(marker.get_absolute_url(), "/marker/6027")


class CemeteryTestCase(TestCase):
    def setUp(self):
        pass

    def test_cemetery_string(self):
        """Verifying __str__ returns with proper formatting."""
        cemetery = models.Cemetery.objects.get(pk=1)
        self.assertEqual(cemetery.__str__(), "Timberidge Cemetery")

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        cemetery = models.Cemetery.objects.get(pk=1)
        self.assertEqual(cemetery.get_absolute_url(), "/cemeteries/1")


class PersonTestCase(TestCase):
    def setUp(self):
        pass

    def test_person_string(self):
        """Verifying __str__ returns with proper formatting."""
        person = models.Person.objects.get(first_name="Alonzo")
        r = "FullName : Alonzo Poole, Markerid: 6006 - Timberidge Cemetery Born: 11th January 1870 Died: 15th May 1935"
        self.assertEqual(person.__str__(), r)

    def get_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        person = models.Person.objects.get(first_name="Alonzo")
        self.assertEqual(person.get_absolute_url(), "/person/3")


class ImageTestCase(TestCase):
    def setUp(self):
        pass

    def test_image_string(self):
        image = models.MarkerImage.objects.get(markerid=6006)
        self.assertEqual(image.__str__(), "Markerid: 6006 - Timberidge Cemetery")


class WWDCTestCase(TestCase):
    """ Verifying __str__ returns with proper formatting."""
    def setUp(self):
        pass

    def test_wwdc_string(self):
        draft = models.WWDC.objects.get(person_id=10)
        self.assertEqual(draft.__str__(), "Ben Poole")


class SymbologyTestCase(TestCase):
    def setup(self):
        pass

    def test_symbology_string(self):
        """Verifying __str__ returns the proper formatting"""
        symbology = models.Symbology.objects.get(symbology="floral")
        self.assertEqual(symbology.__str__(), "floral")


class UrlTests(TestCase):
    """ Verifying that the urls use the correct view.
    """
    def test_main_url(self):
        main = resolve(reverse('cemeteries:main'))
        return self.assertEqual(main.func.__name__,
                                MainView.__name__)

    def test_cem_lview(self):
        cem_lview = resolve(reverse('cemeteries:cem_lview'))
        return self.assertEqual(cem_lview.func.__name__,
                                CemeteryListView.__name__)

    def test_cem_dview(self):
        cem_dview = resolve(reverse('cemeteries:cem_dview', kwargs={'pk': 1}))
        return self.assertEqual(cem_dview.func.__name__,
                                CemeteryDetailView.__name__)

    def test_marker_lview(self):
            marker_lview = resolve(reverse('cemeteries:marker_lview'))
            return self.assertEqual(marker_lview.func.__name__,
                                    MarkerListView.__name__)

    def test_marker_dview(self):
        marker_dview = resolve(reverse('cemeteries:marker_dview', kwargs={'pk': 1}))
        return self.assertEqual(marker_dview.func.__name__,
                                MarkerDetailView.__name__)

    def person_lview(self):
        person_lview = resolve(reverse('cemeteries:person_lview'))
        return self.assertEqual(person_lview.func.__name__,
                                PersonListView.__name__)

    def test_person_dview(self):
        person_dview = resolve(reverse('cemeteries:person_dview', kwargs={'pk': 1}))
        return self.assertEqual(person_dview.func.__name__,
                                PersonDetailView.__name__)

    def test_about_url(self):
        about = resolve(reverse('cemeteries:about'))
        return self.assertEqual(about.func.__name__,
                                AboutView.__name__)

    def test_person_search(self):
        search = resolve(reverse('cemeteries:people_view'))
        return self.assertEqual(search.func.__name__,
                                PeopleView.__name__)

    def test_symbology_ur(self):
        symbology = resolve(reverse('cemeteries:symbology'))
        return self.assertEqual(symbology.func.__name__,
                                SymbologyView.__name__)

    def test_markermap_url(self):
        map = resolve(reverse('cemeteries:markermap'))
        return self.assertEqual(map.func.__name__,
                                MarkerMapView.__name__)

    def test_personmap_url(self):
        map = resolve(reverse('cemeteries:personmap'))
        return self.assertEqual(map.func.__name__,
                                PersonMapView.__name__)

    def test_symbolmap_url(self):
        map = resolve(reverse('cemeteries:symbolmap', kwargs={'pk': 1}))
        return self.assertEqual(map.func.__name__,
                                SymbolMapView.__name__)

    def test_api_people(self):
        people = resolve(reverse('cemeteries_api:people_collection'))
        return self.assertEqual(people.func.__name__,
                                PeopleCollection.__name__)

    def test_api_person(self):
        person = resolve(reverse('cemeteries_api:person_collection', kwargs={'pk': 1}))
        return self.assertEqual(person.func.__name__,
                                PersonCollection.__name__)

    def test_api_markers(self):
        markers = resolve(reverse('cemeteries_api:markers_collection'))
        return self.assertEqual(markers.func.__name__,
                                MarkersCollection.__name__)

    def test_api_marker(self):
        marker = resolve(reverse('cemeteries_api:marker_collection', kwargs={'pk': 1}))
        return self.assertEqual(marker.func.__name__,
                                MarkerCollection.__name__)

    def test_wwdc_url(self):
        draft = resolve(reverse('cemeteries:WWDC_view'))
        return self.assertEqual(draft.func.__name__,
                                WWDCView.__name__)

    def test_wwdcmap_url(self):
        draft = resolve(reverse('cemeteries:WWDC_map'))
        return self.assertEqual(draft.func.__name__,
                                WWDCMapView.__name__)