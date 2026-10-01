class Huone: #Antaa huoneelle nimen ja mahdollisen esineen
    def __init__(self, nimi,selite , esine=None):
        self.nimi = nimi
        self.selite = selite
        self.esine = esine

    def __str__(self): #Palauttaa huoneen nimen ja/tai esineen
        if self.esine:
            return f"{self.nimi} (esine: {self.esine.nimi})"
        return self.nimi