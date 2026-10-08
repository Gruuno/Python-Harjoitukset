class Pelaaja:
    # Antaa pelaajalle nimen, sijainnin, tyhjän esinelistan ja pisteet
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti
        self.pisteet = 0
        self.lajitellut_roskat = []

    def liiku(self, kohde):
        #Liikuttaa pelaajan uuteen huoneeseen
        self.sijainti = kohde

        print(f"\n{self.nimi} liikkuu huoneeseen: {kohde.nimi}")
        print(kohde.selite)

        if kohde.esineet:
            print("\nHuoneessa on seuraavat esineet:")

            for esine in kohde.esineet:
                print(f"- {esine.nimi}")

    def take_item(self):
        #Tarkistaa, onko huoneessa esineitä
        if not self.sijainti.esineet:
            print("Tässä huoneessa ei ole esineitä.")
            return None

        print("\nHuoneessa olevat esineet:")

        for i, esine in enumerate(self.sijainti.esineet, start=1):
            print(f"{i} - {esine.nimi}")

        valinta = input("Minkä esineen haluat kerätä? ")

        if not valinta.isdigit():
            print("Anna numero.")
            return None

        numero = int(valinta)

        if numero < 1 or numero > len(self.sijainti.esineet):
            print("Virheellinen valinta.")
            return None

        #Otetaan valittu esine huoneesta
        esine = self.sijainti.esineet.pop(numero - 1)

        #Lisätään esine pelaajan tavaroihin
        self.esineet.append(esine)

        if esine.onko_roska():
            print(f"Keräsit roskan: {esine.nimi}")
        else:
            print(f"Keräsit esineen: {esine.nimi}")

        return esine

    def onko_esine(self, nimi):
        #Tarkistaa, löytyykö pelaajan tavaroista tietty esine
        for esine in self.esineet:
            if esine.nimi == nimi:
                return True

        return False