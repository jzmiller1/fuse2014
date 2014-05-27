from haystack import indexes
from cemeteries.models import Cemetery, Marker, Person, Symbology


class CemeteryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Cemetery

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


class MarkerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Marker

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


class SymbologyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Symbology

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()
