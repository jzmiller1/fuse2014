from rest_framework import mixins
from rest_framework import generics
import django_filters
from cemeteries.serializers import PersonSerializer, MarkerSerializer
from cemeteries.models import Person, Marker


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type):integers})
        return qs


class MarkerFilter(django_filters.FilterSet):
    markerid = IntegerListFilter(name='markerid', lookup_type='in')

    class Meta:
        model = Marker
        fields = ['cemetery', 'markerid', 'condition', 'readable', 'epitaph', 'family_name']


class PersonFilter(django_filters.FilterSet):
    markerid = IntegerListFilter(name='markerid', lookup_type='in')

    class Meta:
        model = Person
        fields = ['markerid', 'full_name', 'first_name', 'last_name', 'gender', 'veteran', 'b_year',
                  'd_year', 'a_birth', 'a_death', 'epitaph', 'footstone', 'footstoneI']


class PeopleCollection(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_class = PersonFilter


class PersonCollection(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MarkersCollection(generics.ListAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    filter_class = MarkerFilter


class MarkerCollection(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)