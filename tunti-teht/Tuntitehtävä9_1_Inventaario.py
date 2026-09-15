import random

class Inventaario:
    def __init__(self):
        #Aloitus loitsu ja reppu
        self.loitsut = ["Tulipallo"]
        self.reppu = {}

        #Mahdolliset laadut
        self.laadut = ("Hyvä", "Keskinkertainen", "Huono")

        self.lisaa_aloitustavarat()

    def lisaa_aloitustavarat(self): #Lisää aloitus kamat satunnaisilla laaduilla
        self.reppu["Miekka"] = random.choice(self.laadut)
        self.reppu["Kilpi"] = random.choice(self.laadut)

    def lisaa_reppuun(self, tavara): #Lisää uude tavara reppuun ja antaa satunnaisen laadun.
        if tavara in self.reppu:
            print(f"-> Sinulla on jo tavara: {tavara}.")
            return

        laatu = random.choice(self.laadut)
        self.reppu[tavara] = laatu

        print(f"-> Lisätty reppuun: {tavara} (Laatu: {laatu})")

    def lisaa_loitsu(self, loitsu): #Lisää uude loitsun ja katsoo onko se jo lisätty
        if loitsu not in self.loitsut:
            self.loitsut.append(loitsu)
            print(f"-> Opit uuden loitsun: {loitsu}!")
        else:
            print(f"-> Osaat jo loitsun: {loitsu}.")

    def tulosta_loitsut(self): #Tulostaa opitut loitsut
        print("\nInventaarion loitsut:")

        for loitsu in self.loitsut:
            print(f"- {loitsu}")

    def tulosta_reppu(self): #Tulostaa repun sisällö
        print("\nRepun sisältö:")

        if not self.reppu:
            print("- Reppu on tyhjä.")
            return

        for tavara, laatu in self.reppu.items():
            print(f"- {tavara} (Laatu: {laatu})")


#Pääohjelma
if __name__ == "__main__":
    oma_inventaario = Inventaario()

    #Tulostetaan alkutilanne
    print("--- PELI ALKAA ---")
    oma_inventaario.tulosta_loitsut()
    oma_inventaario.tulosta_reppu()

    #Interaktiivinen valikko
    while True:
        print("\n--- MITÄ HALUAT TEHDÄ? ---")
        print("1. Lisää tavara reppuun")
        print("2. Opettele uusi loitsu")
        print("3. Katso inventaario")
        print("4. Lopeta ohjelma")

        valinta = input("Valitse toiminto (1-4): ").strip()

        if valinta == "1":
            tavara = input("Syötä lisättävän tavaran nimi: ").strip()

            if tavara:
                oma_inventaario.lisaa_reppuun(tavara)
            else:
                print("Tavaran nimi ei voi olla tyhjä!")

        elif valinta == "2":
            loitsu = input("Syötä opittavan loitsun nimi: ").strip()

            if loitsu:
                oma_inventaario.lisaa_loitsu(loitsu)
            else:
                print("Loitsun nimi ei voi olla tyhjä!")

        elif valinta == "3":
            oma_inventaario.tulosta_loitsut()
            oma_inventaario.tulosta_reppu()

        elif valinta == "4":
            print("\nLopetetaan... Tässä on lopullinen inventaario:")
            oma_inventaario.tulosta_loitsut()
            oma_inventaario.tulosta_reppu()
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")