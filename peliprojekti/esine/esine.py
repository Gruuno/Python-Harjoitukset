class Esine: #Antaa esineelle nimen ja painon
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

    def __str__(self): #Palauttaa esineen nimen ja painon
        return f"{self.nimi} ({self.paino} kg)"