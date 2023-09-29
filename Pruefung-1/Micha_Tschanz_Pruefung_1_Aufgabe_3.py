class Stadt:
    def __init__(self, name, land, kontinent, einwohnerzahl = 0, koordinate = (0,0)):
        self.name = name
        self.einwohnerzahl =einwohnerzahl
        self.land = land
        self.kontinent = kontinent
        self.koordinate = koordinate
    
    def __str__(self):
        return self.name