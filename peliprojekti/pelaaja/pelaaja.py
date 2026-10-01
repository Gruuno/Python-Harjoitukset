class Pelaaja: #Antaa pelaajalle "nimen", ja sijainnin, sekä "esineet" listan
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, kohde):#Liikuttaa pelaajan sijaintia huoneesta toiseen
        self.sijainti = kohde

        print(f"\n{self.nimi} liikkuu huoneeseen: {kohde.nimi}")
        print(kohde.selite)

        if kohde.esine is not None:
            print(f"Huomaat huoneessa esineen: {kohde.esine.nimi}")

    def take_item(self): #Kerää esineen huoneest jos sitä edes on.
        if self.sijainti.esine is not None:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f"Keräsit esineen: {esine.nimi}")
        else:
            print("Tässä huoneessa ei ole esinettä.")