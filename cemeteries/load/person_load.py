import shapefile
from cemeteries.models import Person, Cemetery,Marker
import django
django.setup()


person_path = 'C:/Users/Crystal/Desktop/ShapefileEdits/Person_Master.shp'

sf = shapefile.Reader(person_path)
sr = sf.shapeRecords()


for r in sr:
    mid = Marker.objects.filter(markerid=r.record[0]).first()
    birth = r.record[23]
    death = r.record[24]
    if birth.startswith('0000') or birth[5:7] == '00':
        birth = None
    if death.startswith('0000') or death[5:7] == '00':
        death = None
    m = Person(markerid=mid, full_name=r.record[22], first_name=r.record[2],
               last_name=r.record[1], gender=r.record[5], veteran=r.record[6],
               b_year=r.record[7], d_year=r.record[10], a_birth=birth,
               a_death=death, epitaph=r.record[13], footstone=r.record[14],
               footstoneI=r.record[15], point="POINT({} {})".format(r.shape.points[0][0], r.shape.points[0][1]))
    print(r.record)
    m.save()
