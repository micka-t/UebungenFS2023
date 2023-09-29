class WGS84Coord:
    def __init__(self, lng=0, lat=0):
        self.setLongitude(lng)
        self.setLatitude(lat)
    
    def setLongitude(self, lng):
    
    def setLatitude(self, lat):
        if lat > 90:
            self._lat = lat - 180*(1+(lat +90))
        elif lat < -90:
            self._lat = -90 - (lat +90)
        else:
            self._lat = lat
    
    def getLongitude(self):
        return self._lng
    
    def getLatitude(self):
        return self._lat


pos1 = WGS84Coord(8.5,47.3)

print(pos1._lng, pos1._lat)