from cemeteries.models import Symbology, Marker
import django
django.setup()

symbology_path = 'C:/Users/Crystal/Desktop/CemData/symbology.csv'

f = open(symbology_path, 'r')
data = f.readlines()
f.close()
for line in data[1:]:
    markerid, symbol = line.strip().split(',')
    symbology = Symbology.objects.filter(symbology=symbol).first()
    marker = Marker.objects.filter(markerid=markerid).first()
    if marker is not None:
        if symbology is not None:
            symbology.markers.add(marker)
            symbology.save()

        else:
            new_symbol = Symbology(symbology=symbol)
            new_symbol.save()
            new_symbol.markers.add(marker)
            new_symbol.save()
    else:
        fmarker = []
        fmarker.append(markerid)
        print ("Failed: {}".format(fmarker))