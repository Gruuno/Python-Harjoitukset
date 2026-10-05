from pathlib import Path

from esine.esine import Esine
from huone.huone import Huone
from pelaaja.pelaaja import Pelaaja

BASE_DIR = Path(__file__).resolve().parent
SAVE_DIR = BASE_DIR / "tallennukset"


def show_menu(): #Pelin "valikko"
    print("\n-|- VALIKKO -|-")
    print("1 - Liiku huoneeseen")
    print("2 - Kerää esine")
    print("3 - Näytä esineet")
    print("4 - Näytä nykyinen sijainti")
    print("0 - Lopeta peli")


def lue_tiedosto(tiedostonimi): #Lukee annetun tiedoston sisällön ja antaa sen merkkijonona. Jos tiedostoa ei löydy, palauttaa virheilmoituksen.
    tiedosto = BASE_DIR / tiedostonimi

    try:
        with open(tiedosto, "r", encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except FileNotFoundError:
        return f"Tiedostoa {tiedostonimi} ei löytynyt."


# |----------------------------------------------------------------------|
# Tallentaa pelaajan nimen, sijainnin ja esineet jos näitä on
def tallenna_peli(pelaaja):

    #Luodaan tallennuskansio, jos sitä ei vielä ole
    SAVE_DIR.mkdir(exist_ok=True)

    #Poistetaan nimestä sellaiset merkit, joita ei haluta tiedostonimeen
    turvallinen_nimi = "".join(
        merkki for merkki in pelaaja.nimi
        if merkki.isalnum() or merkki in "_-"
    )

    if not turvallinen_nimi:
        turvallinen_nimi = "pelaaja"

    tallennus_tiedosto = SAVE_DIR / f"{turvallinen_nimi}.txt"

    with open(tallennus_tiedosto, "w", encoding="utf-8") as tiedosto:
        tiedosto.write(f"nimi={pelaaja.nimi}\n")
        tiedosto.write(f"sijainti={pelaaja.sijainti.nimi}\n")

        esineiden_nimet = [esine.nimi for esine in pelaaja.esineet]
        tiedosto.write(f"esineet={','.join(esineiden_nimet)}\n")

    print("Peli tallennettu.")
# |----------------------------------------------------------------------|



# |----------------------------------------------------------------------|
# Ladataan pelaajan aiemmin tallennettu peli, jos sellainen on olemassa
def lataa_peli(nimi, rooms, esineet):
    turvallinen_nimi = "".join(
        merkki for merkki in nimi
        if merkki.isalnum() or merkki in "_-"
    )

    if not turvallinen_nimi:
        turvallinen_nimi = "pelaaja"

    tallennus_tiedosto = SAVE_DIR / f"{turvallinen_nimi}.txt"

    if not tallennus_tiedosto.exists():
        return None

    try:
        with open(tallennus_tiedosto, "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()

        tallennetut_tiedot = {}

        for rivi in rivit:
            rivi = rivi.strip()

            if "=" in rivi:
                avain, arvo = rivi.split("=", 1)
                tallennetut_tiedot[avain] = arvo

        #Hakee tallennetun sijainnin
        sijainti_nimi = tallennetut_tiedot.get("sijainti")

        sijainti = None

        for huone in rooms:
            if huone.nimi == sijainti_nimi:
                sijainti = huone
                break

        if sijainti is None:
            print("Tallennettua sijaintia ei löytynyt.")
            return None

        #Luodaan pelaaja tallennetuilla tiedoilla
        pelaaja = Pelaaja(nimi, sijainti)

        #Hakee tallennetut esineet pelaajalle
        esineiden_nimet = tallennetut_tiedot.get("esineet", "")

        if esineiden_nimet:
            tallennetut_esineet = esineiden_nimet.split(",")
        else:
            tallennetut_esineet = []

        #Lisätään pelaajalle tallennetut esineet
        for esine in esineet:
            if esine.nimi in tallennetut_esineet:
                pelaaja.esineet.append(esine)

        #Poistetaan kerätyt esineet huoneista
        for huone in rooms:
            if huone.esine is not None:
                if huone.esine.nimi in tallennetut_esineet:
                    huone.esine = None

        print("Tallennus ladattu onnistuneesti.")
        return pelaaja

    except (OSError, ValueError):
        print("Tallennuksen lataaminen epäonnistui.")
        return None
# |----------------------------------------------------------------------|



def main():

    # |----------------------------------------------------------------------|
    # Tulostetaan pelin "intro" ja "ohjeet" tekstitiedostot

    print(lue_tiedosto("intro.txt"))
    print("\n")
    print(lue_tiedosto("ohjeet.txt"))

    print("\n----------------------------------------")
    # |----------------------------------------------------------------------|



    # |----------------------------------------------------------------------|
    #Luotuja esineitä
    Flashlight = Esine("Taskulamppu", 0.5)
    Key1 = Esine("Avain", 0.1)
    Book = Esine("Kirja", 1.0)
    Typewriter = Esine("Typewriter", 21.0)
    # |----------------------------------------------------------------------|



    # |----------------------------------------------------------------------|
    #Luotuja huoneita
    entryway = Huone(
        "Eteinen",
        "Pieni ja hämärä, maali on kulunut ja lattialla oleva "
        "\"WELCOME\" matto ei ole nähnyt pesua aikoihin.\n"
        "Huomaat myös, että eteisessä on naulakko jossa on pölyn "
        "peittämä takki ja hattu."
    )

    kitchen = Huone(
        "Keittiö",
        "Vanha keittiö, huone tuntuu kylmältä ja kostealta. "
        "Vaikka home on tuhonnut suurimman osan keittiön kaapeista, "
        "pystyt silti näkemään, että keittiö on ollut jossakin "
        "vaiheessa hyvin varusteltu.",
        Flashlight
    )

    study = Huone(
        "Kirjasto",
        "Kirjasto on erittäin vanha ja pölyinen. "
        "Kirjahyllyt ovat täynnä kirjoja, mutta suurin osa niistä "
        "on joko homeessa tai yökkösten syömiä.",
        Book
    )

    storage = Huone(
        "Varasto",
        "Ahdas ja tunkkainen varasto, näkemästä päätellen "
        "varmaan käytetty pikkuvarastona. Varaston hyllyt ovat "
        "täynnä vanhoja tavaroita, mutta suurin osa niistä on "
        "joko rikkinäisiä tai homeessa.",
        Key1
    )
    # |----------------------------------------------------------------------|



    # |----------------------------------------------------------------------|
    # Määritellään huoneiden väliset yhteydet
    rooms = [entryway, kitchen, study, storage]

    esineet = [Flashlight, Key1, Book, Typewriter]

    nimi = input("\nAnna pelaajan nimi: ")
    # |----------------------------------------------------------------------|



    # |----------------------------------------------------------------------|
    # Ladataan aiemmin tallennettu peli, jos sellainen on edes olemassa
    pelaaja = lataa_peli(nimi, rooms, esineet)

    if pelaaja is None: #Jos viimeksi pelattu peliä ei löydy, luodaan uusi pelaaja
        pelaaja = Pelaaja(nimi, entryway)
        print(f"\nUusi peli aloitettu. Tervetuloa peliin, {pelaaja.nimi}!")

    else:
        print(f"\nTervetuloa takaisin, {pelaaja.nimi}!")
        print(f"Jatkat huoneesta: {pelaaja.sijainti.nimi}")
    # |----------------------------------------------------------------------|



    # |----------------------------------------------------------------------|
    # Pelin itse pääsilmukka
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


        elif valinta == "2": #Kerää esineen jos sellainen huoneessa on
            pelaaja.take_item()


        elif valinta == "3": #Näytä pelaajan esineet
            print("\n-|- ESINEET -|-")

            if len(pelaaja.esineet) == 0:
                print("Sinulla ei ole esineitä.")
            else:
                for esine in pelaaja.esineet:
                    print(f"- {esine.nimi} ({esine.paino} kg)")


        elif valinta == "4": #Näytä pelaajan nykyinen sijainti
            print(f"\nOlet huoneessa: {pelaaja.sijainti.nimi}")
            print(pelaaja.sijainti.selite)

            if pelaaja.sijainti.esine is not None:
                print(
                    f"Huoneessa on esine: "
                    f"{pelaaja.sijainti.esine.nimi}"
                )
            else:
                print("Huoneessa ei ole esinettä.")

        elif valinta == "0":
            tallenna_peli(pelaaja) #Tallentaa varmuudeksi jos peli lopetetaan

            print("Peli lopetettu. Kiitos pelaamisesta!")
            break

        else: #Failsafe jos pelaaja syöttää jotain muuta kuin 0-4
            print(
                "Virheellinen valinta. "
                "Sinun pitää valita numero väliltä 0-4."
            )

        #Tallentaa peli jokaisen toiminnon jälkeen
        tallenna_peli(pelaaja)
    # |----------------------------------------------------------------------|


if __name__ == "__main__":
    main()