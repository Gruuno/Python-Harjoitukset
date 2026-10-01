from esine.esine import Esine
from huone.huone import Huone
from pelaaja.pelaaja import Pelaaja


def show_menu():
    print("\n-|- VALIKKO -|-")
    print("1 - Liiku huoneeseen")
    print("2 - Kerää esine")
    print("3 - Näytä esineet")
    print("4 - Näytä nykyinen sijainti")
    print("0 - Lopeta peli")


def main():
    #Luo esineitä
    Flashlight = Esine("Taskulamppu", 0.5)
    Key1 = Esine("Avain", 0.1)
    Book = Esine("Kirja", 1.0)
    Typewriter = Esine("Typewriter", 21.0)


    #Luo huoneet + pikku selitys
    entryway = Huone(
    "Eteinen",
    "Pieni ja hämärä, maali on kulunut ja lattialla oleva \"WELCOME\" matto ei ole nähnyt pesua aikoihin.\nHuomaat myös, että eteisessä on naulakko jossa on pölyn peittämä takki ja hattu."
    )

    kitchen = Huone(
    "Keittiö",
    "Vanha keittiö, huone tuntuu kylmältä ja kostealta. Vaikka home on tuhonnut suurimman osan keittiön kaapeista, pystyt silti näkemään, että keittiö on ollut jossakin vaiheessa hyvin varusteltu.",
    Flashlight
    )

    study = Huone(
    "Kirjasto",
    "Kirjasto on erittäin vanha ja pölyinen. Kirjahyllyt ovat täynnä kirjoja, mutta suurin osa niistä on joko homeessa tai yökkösten syömiä.",
    Book
    )

    storage = Huone(
    "Varasto",
    "Ahdas ja tunkkainen varasto, näkemästä päätelleen varmaan käytetty pikkuvarastona. Varaston hyllyt ovat täynnä vanhoja tavaroita, mutta suurin osa niistä on joko rikkinäisiä tai homeessa.",
    Key1
    )

    #Lisää huoneet listaan
    rooms = [entryway, kitchen, study, storage]

    #Luo itse pelaaja ja aloittaa hänet eteisestä
    pelaaja = Pelaaja(input("Anna pelaajan nimi: "), entryway)

    print(f"Tervetuloa peliin, {pelaaja.nimi}!")

    while True:
        show_menu()

        valinta = input("Valitse toiminto: ")

        if valinta == "1": #Liiku huoneeseen
            print("\n-|- HUONEET -|-")

            for i, huone in enumerate(rooms, start=1):
                if huone == pelaaja.sijainti:
                    print(f"{i} - {huone.nimi} (olet täällä)")
                else:
                    print(f"{i} - {huone.nimi}")

            huone_valinta = input("Mihin huoneeseen haluat mennä? ")

            if huone_valinta.isdigit():
                numero = int(huone_valinta)

                if 1 <= numero <= len(rooms):
                    kohde = rooms[numero - 1]

                    if kohde == pelaaja.sijainti:
                        print("Olet jo tässä huoneessa.")
                    else:
                        pelaaja.liiku(kohde)
                else:
                    print("Virheellinen huonevalinta.")
            else:
                print("Anna numero.")

        elif valinta == "2": #Kerää esine
            pelaaja.take_item()

        elif valinta == "3": #Näytä esineet
            print("\n-|- ESINEET -|-")

            if len(pelaaja.esineet) == 0:
                print("Sinulla ei ole esineitä.")
            else:
                for esine in pelaaja.esineet:
                    print(f"- {esine.nimi} ({esine.paino} kg)")

        elif valinta == "4": #Näytä nykyinen sijainti
            print(f"\nOlet huoneessa: {pelaaja.sijainti.nimi}")
            print(pelaaja.sijainti.selite)

            if pelaaja.sijainti.esine is not None:
                print(f"Huoneessa on esine: {pelaaja.sijainti.esine.nimi}")
            else:
                print("Huoneessa ei ole esinettä.")

        elif valinta == "0": #Lopeta peli
            print("Peli lopetettu. Moikka!")
            break

        else:
            print("Virheellinen valinta. Sinun pitää valita numero väliltä 0-4.")


if __name__ == "__main__":
    main()