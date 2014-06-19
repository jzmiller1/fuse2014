from django.forms import widgets
from rest_framework_gis import serializers
from .models import Person, Marker


class PersonSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Person
        geo_field = "point"
        fields = ('id', 'markerid', 'full_name', 'first_name', 'last_name', 'gender', 'veteran', 'b_year',
                    'd_year', 'a_birth', 'a_death', 'epitaph', 'footstone', 'footstoneI')


class MarkerSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Marker
        geo_field = 'point'
        fields = ('cemetery', 'markerid', 'condition', 'readable', 'epitaph', 'family_name')
