from rest_framework import mixins
from rest_framework import generics
from cemeteries.serializers import PersonSerializer, MarkerSerializer
from cemeteries.models import Person, Marker


class PeopleCollection(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonCollection(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MarkersCollection(generics.ListCreateAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


class MarkerCollection(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)