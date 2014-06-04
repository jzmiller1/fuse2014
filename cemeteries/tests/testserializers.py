from django.test import TestCase
import unittest
from cemeteries.models import Person
from cemeteries.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from collections import OrderedDict


class PersonSerializer_Tests(TestCase):

    def test_model_to_dictionary(self):
        person = Person.objects.get(first_name="Alonzo")
        serializer = PersonSerializer(person)
        expected_dict = {'markerid': person.markerid,
                        'full_name': person.full_name,
                        'first_name': person.first_name,
                        'last_name': person.last_name,
                        'gender': person.gender,
                        'veteran': person.veteran,
                        'b_year': person.b_year,
                        'd_year': person.d_year,
                        'a_birth': person.a_birth,
                        'a_death': person.a_death,
                        'epitaph': person.epitaph,
                        'footstone': person.footstone,
                        'footstoneI': person.footstoneI,
                        }
        self.assertEquals(expected_dict, serializer.data)

    def test_dictionary_to_json(self):
        person = Person.objects.get(first_name="Alonzo")
        serializer = PersonSerializer(person)
        content = JSONRenderer().render(serializer.data)
        print(content)
        expected_dict = OrderedDict([('markerid', person.markerid.markerid),
                                     ('full_name', person.full_name),
                                     ('first_name', person.first_name),
                                     ('last_name', person.last_name),
                                     ('gender', person.gender),
                                     ('veteran', person.veteran),
                                     ('b_year', person.b_year),
                                     ('d_year', person.d_year),
                                     ('a_birth', person.a_birth),
                                     ('a_death', person.a_death),
                                     ('epitaph', person.epitaph),
                                     ('footstone', person.footstone),
                                     ('footstoneI', person.footstoneI),
                                     ])

        expected_json = JSONRenderer().render(expected_dict)

        self.assertEquals(expected_json, content)