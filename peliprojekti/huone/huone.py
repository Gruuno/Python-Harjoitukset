class Huone: 
    #Antaa huoneelle nimen, selitteen ja listan esineitä
    def __init__(self, nimi, selite, esineet=None):
        self.nimi = nimi
        self.selite = selite

        if esineet is None:
            self.esineet = []
        else:
            self.esineet = esineet

    def __str__(self): 
        #Palauttaa huoneen nimen ja huoneessa olevat esineet
        if self.esineet:
            nimet = ", ".join(esine.nimi for esine in self.esineet)
            return f"{self.nimi} (esineet: {nimet})"

        return self.nimi