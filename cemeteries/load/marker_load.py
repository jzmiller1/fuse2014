import shapefile
from cemeteries.models import Marker, Cemetery
import django
django.setup()

marker_path = 'C:/Users/Crystal/Desktop/ShapefileEdits/marker/MarkerMaster.shp'
person_path = 'C:/Users/Crystal/Desktop/ShapefileEdits/Person_Master.shp'

sf = shapefile.Reader(marker_path)
sr = sf.shapeRecords()
cem = Cemetery.objects.filter(pk=1).first()

for r in sr:

    m = Marker(cemetery=cem, markerid=r.record[0], condition=r.record[1],
               readable=r.record[2], epitaph=r.record[3], family_name=r.record[4],
               point="POINT({} {})".format(r.shape.points[0][0], r.shape.points[0][1]))
    print(r.record[0], r.record[1], r.record[2], r.record[3], r.record[4], r.shape.points)
    m.save()