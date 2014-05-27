from django.db import models
from django_date_extensions.fields import ApproximateDateField, ApproximateDate


class Cemetery(models.Model):
    """ Cemetery model.

    Represents a cemetery.

    """
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return "{} Cemetery".format(self.name)

    def get_absolute_url(self):
        return "/cemeteries/{}".format(self.pk)


class Marker(models.Model):
    """ Marker Model.

    Represents a cemetery marker (gravestone).

    """
    cemetery = models.ForeignKey(Cemetery)
    markerid = models.IntegerField(primary_key=True)
    condition = models.CharField(max_length=15)
    readable = models.BooleanField(default=None)
    epitaph = models.CharField(max_length=20)
    family_name = models.CharField(max_length=20)

    def __str__(self):
        return "Markerid: {} - {}".format(self.markerid, self.cemetery)

    def get_absolute_url(self):
        return "/marker/{}".format(self.markerid)


class Person(models.Model):
    """ Person Model.

    Represents a person interred at a cemetery and connects them to their Marker.

    """

    markerid = models.ForeignKey(Marker)
    full_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=7)
    veteran = models.CharField(max_length=7)
    b_year = models.CharField(max_length=4)
    d_year = models.CharField(max_length=4)
    a_birth = ApproximateDateField(null=True)
    a_death = ApproximateDateField(null=True)
    epitaph = models.TextField()
    footstone = models.BooleanField(default=None)
    footstoneI = models.TextField()

    def __str__(self):
        return "FullName : {0}, {1} Born: {2} Died: {3}".format(self.full_name, self.markerid, self.a_birth,self.a_death)

    def get_absolute_url(self):
        return "/person/{}".format(self.pk)


class MarkerImage(models.Model):
    """ MarkerImage Model

    Represents an image of a marker.

    """
    markerid = models.ForeignKey(Marker)
    image = models.ImageField()

    def __str__(self):
        return "{}".format(self.markerid)


class Symbology(models.Model):
    """ Symbology Model

    """

    symbology = models.CharField(max_length=40)
    markers = models.ManyToManyField(Marker, blank=True)

    def __str__(self):
        return "{0}".format(self.symbology)