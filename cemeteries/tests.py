from django.test import TestCase

# Create your tests here.
from django.test import TestCase
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


class CemeteryTestCase(TestCase):
    def setUp(self):
        pass

    def test_cemetery_string(self):
        """Verifying __str__ returns with proper formatting."""
        cemetery = models.Cemetery.objects.get(pk=1)
        self.assertEqual(cemetery.__str__(), "Timberidge Cemetery")


class PersonTestCase(TestCase):
    def setUp(self):
        pass

    def test_person_string(self):
        """Verifying __str__ returns with proper formatting."""
        person = models.Person.objects.get(first_name="Alonzo")
        self.assertEqual(person.__str__(), "FullName : Alonzo Poole, Markerid: 6006 - Timberidge Cemetery")