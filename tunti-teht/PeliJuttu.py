class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.oikea = None
        self.vasen = None
        self.eteen = None
        self.taakse = None


class Peli:
    def __init__(self):
        #Huoneet
        eteinen = Huone("eteinen")
        keittio = Huone("keittiö")
        olohuone = Huone("olohuone")
        kellari = Huone("kellari")

        #Eteinen
        eteinen.vasen = keittio
        eteinen.oikea = olohuone
        eteinen.eteen = kellari
        eteinen.taakse = None

        #Keittiö
        keittio.vasen = None
        keittio.oikea = eteinen
        keittio.eteen = None
        keittio.taakse = None

        #Olohuone
        olohuone.vasen = eteinen
        olohuone.oikea = None
        olohuone.eteen = None
        olohuone.taakse = None

        #Kellari
        kellari.taakse = eteinen
        kellari.vasen = None
        kellari.oikea = None
        kellari.eteen = None

        #Kaikki olemassa olevat huoneet
        self.huoneet = [eteinen, keittio, olohuone, kellari]

        #Aloitushuone
        self.nykyinen_huone = eteinen

        #Aloittaa pelin
        self.pelaa()

    def pelaa(self):
        while True:
            print("\nOlet huoneessa:", self.nykyinen_huone.nimi)

            komento = input(
                "Anna suunta (vasen, oikea, eteen, taakse) tai q: "
            ).strip().lower()

            if komento == "q":
                print("Peli loppui.")
                break

            if komento == "vasen":
                uusi_huone = self.nykyinen_huone.vasen

            elif komento == "oikea":
                uusi_huone = self.nykyinen_huone.oikea

            elif komento == "eteen":
                uusi_huone = self.nykyinen_huone.eteen

            elif komento == "taakse":
                uusi_huone = self.nykyinen_huone.taakse

            else:
                print("\nVirheellinen komento.")
                continue

            if uusi_huone is None:
                print("\nSeinä! Et voi mennä siihen suuntaan.")
            else:
                self.nykyinen_huone = uusi_huone
                print("\nSiirryit huoneeseen:", uusi_huone.nimi)

Peli()