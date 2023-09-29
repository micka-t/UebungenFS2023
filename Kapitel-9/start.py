from pyproj import Transformer

lat = 47.5347
lng = 7.64240

t = Transformer.from_crs("EPSG:4326", "EPSG:2056")

r = t.transform(lat, lng)

print(r)
#    2615344.1410226785, 1264905.3517398122
t2 = Transformer.from_crs("EPSG:2056", "EPSG:4326")

r2 = t2.transform(2615344.1410226785, 1264905.3517398122)

print(r2)