class Esine: 
    #Antaa esineelle nimen, painon ja mahdollisen jätelajin
    def __init__(self, nimi, paino, jatelaji=None):
        self.nimi = nimi
        self.paino = paino
        self.jatelaji = jatelaji

    def onko_roska(self):
        #Jos esineellä on jätelaji, se on roska, muuten ei
        return self.jatelaji is not None

    def __str__(self): 
        #Palauttaa esineen nimen ja painon
        return f"{self.nimi} ({self.paino} kg)"