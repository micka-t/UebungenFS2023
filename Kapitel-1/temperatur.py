class Temperatur():
    def __init__(self, c):
        self.setTemperatur(c)

    def getKelvin(self):
        return self._celsius + 273.15
    
    def setKelvin(self, value):
        self._celsius = value - 273.15
       
    def setTemperatur(self, value):
        if value < -273.15:
            raise ValueError("Die Temperatur darf nicht kleiner als -273.15℃ sein.")   
        self._celsius = value

    def getTemperatur(self):
        return self._celsius
    
    celsius = property(getTemperatur, setTemperatur)
    kelvin = property(getKelvin, setKelvin)

basel = Temperatur(7)
basel.kelvin = 285
print(basel.celsius)

