from django.contrib import admin
from .models import Cemetery, Person, Marker, MarkerImage, Symbology, WWDC

# Register your models here.
admin.site.register(Cemetery)
admin.site.register(Person)
admin.site.register(Marker)
admin.site.register(MarkerImage)
admin.site.register(Symbology)
admin.site.register(WWDC)