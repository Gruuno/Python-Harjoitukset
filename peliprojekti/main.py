from pathlib import Path

from esine.esine import Esine
from huone.huone import Huone
from pelaaja.pelaaja import Pelaaja

BASE_DIR = Path(__file__).resolve().parent
SAVE_DIR = BASE_DIR / "tallennukset"

pelinum = 1 #Tyhmä mutta toimii tähän hätään. Estää pelin alussa intro ja ohjeet tulostumasta uudelleen.

def show_menu():#Pelin "valikko"
    print("\n-|- VALIKKO -|-")
    print("1 - Liiku huoneeseen")
    print("2 - Kerää esine")
    print("3 - Näytä esineet")
    print("4 - Näytä nykyinen sijainti")
    print("5 - Lajittele roskia")
    print("6 - Näytä pisteet")
    print("0 - Lopeta peli")


def lue_tiedosto(tiedostonimi): 
    #Lukee annetun tiedoston sisällön ja antaa sen merkkijonona. Jos tiedostoa ei löydy, palauttaa virheilmoituksen.
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
        tiedosto.write(f"pisteet={pelaaja.pisteet}\n")
        tiedosto.write(f"lajitellut={','.join(pelaaja.lajitellut_roskat)}\n")

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
            huone.esineet = [
                esine
                for esine in huone.esineet
                if esine.nimi not in tallennetut_esineet
            ]

        print("Tallennus ladattu onnistuneesti.")
        return pelaaja

    except (OSError, ValueError):
        print("Tallennuksen lataaminen epäonnistui.")
        return None
# |----------------------------------------------------------------------|



# |----------------------------------------------------------------------|
#Lajittelu Funktio?

def lajittele_roskat(pelaaja):
    #Roskat voi lajitella vain eteisessä
    if pelaaja.sijainti.nimi != "Eteinen":
        print("\nRoskat voi lajitella vain eteisessä.")
        return False

    #Etsii pelaajan tavaroista VAIN roskat, jota ei ole vielä lajiteltu
    roskat = [
        esine for esine in pelaaja.esineet
        if esine.onko_roska()
    ]

    if not roskat:
        print("\nSinulla ei ole lajiteltavia roskia.")
        return False

    print("\n-|- LAJITTELU -|-")
    print("Valitse lajiteltava roska:")

    for i, esine in enumerate(roskat, start=1):
        print(f"{i} - {esine.nimi}")

    valinta = input("Valitse roska: ")

    if not valinta.isdigit():
        print("Anna numero.")
        return False

    numero = int(valinta)

    if numero < 1 or numero > len(roskat):
        print("Virheellinen valinta.")
        return False

    esine = roskat[numero - 1]

    print(f"\nMihin lajittelet esineen '{esine.nimi}'?")
    print("1 - Muovi")
    print("2 - Lasi")
    print("3 - Paperi")
    print("4 - Kartonki")
    print("5 - Metalli")
    print("6 - Vaarallinen jäte")
    print("7 - Sähkölaitteet")

    lajittelu = input("Valitse jätelaji: ")

    jatelajit = {
        "1": "muovi",
        "2": "lasi",
        "3": "paperi",
        "4": "kartonki",
        "5": "metalli",
        "6": "vaarallinen jäte",
        "7": "sahkolaitteet"
    }

    if lajittelu not in jatelajit:
        print("Virheellinen lajittelu.")
        return False

    valittu_laji = jatelajit[lajittelu]

    #Merkitsee roskan käsitellyksi
    pelaaja.lajitellut_roskat.append(esine.nimi)

    #Poistaa roskan pelaajan inventorista
    pelaaja.esineet.remove(esine)

    if valittu_laji == esine.jatelaji:
        pelaaja.pisteet += 1
        print(f"\nOikein! {esine.nimi} kuuluu jätelajiin {valittu_laji}.")
        print(f"Sait pisteen! Pisteet: {pelaaja.pisteet}")
    else:
        print(
            f"\nVäärin! {esine.nimi} ei kuulu jätelajiin "
            f"{valittu_laji}."
        )
        print(f"Oikea jätelaji olisi ollut: {esine.jatelaji}")

    return True
#|----------------------------------------------------------------------|



def main(): #Pelin pääfunktio alkaa tästä

# |----------------------------------------------------------------------|
# Tulostetaan pelin "intro" ja "ohjeet" tekstitiedostot
    if pelinum == 1:
        print("\n")
        print(lue_tiedosto("intro.txt"))
        print("\n")
        print(lue_tiedosto("ohjeet.txt"))

        print("\n----------------------------------------")
# |----------------------------------------------------------------------|



# |----------------------------------------------------------------------|
#Esineet ja roskat

# Tavallisia esineitä
Flashlight = Esine("Taskulamppu", 0.5)
Key1 = Esine("Avain", 0.1)
Book = Esine("Kirja", 1.0)
Paristo = Esine("Paristo", 0.1)

# Roskia
Muovipullo = Esine("Muovipullo", 0.1, "muovi")
Lasipurkki = Esine("Lasipurkki", 0.3, "lasi")
Sanomalehti = Esine("Sanomalehti", 0.2, "paperi")
Pahvilaatikko = Esine("Pahvilaatikko", 0.5, "kartonki")
Sailkepurkki = Esine("Säilykepurkki", 0.2, "metalli")
Typewriter = Esine("Kirjoituskone", 21.0, "sahkolaitteet")
Muovipussi = Esine("Muovipussi", 0.1, "muovi")
# |----------------------------------------------------------------------|



# |----------------------------------------------------------------------|
#Luotuja huoneita
entryway = Huone(
    "Eteinen",
    "Pieni ja hämärä, maali on kulunut ja lattialla oleva "
    "\"WELCOME\" matto ei ole nähnyt pesua aikoihin.\n"
    "Huomaat myös, että eteisessä on naulakko jossa on pölyn "
    "peittämä takki ja hattu.",
    [Muovipullo]
)

kitchen = Huone(
    "Keittiö",
    "Vanha keittiö, huone tuntuu kylmältä ja kostealta. "
    "Vaikka home on tuhonnut suurimman osan keittiön kaapeista, "
    "pystyt silti näkemään, että keittiö on ollut jossakin "
    "vaiheessa hyvin varusteltu.",
    [Flashlight, Lasipurkki, Sailkepurkki]
)

study = Huone(
    "Kirjasto",
    "Kirjasto on erittäin vanha ja pölyinen. "
    "Kirjahyllyt ovat täynnä kirjoja, mutta suurin osa niistä "
    "on joko homeessa tai yökkösten syömiä.",
    [Book, Sanomalehti, Pahvilaatikko, Paristo]
)

storage = Huone(
    "Varasto",
    "Ahdas ja tunkkainen varasto. Täällä on selvästi säilytetty "
    "vanhoja tavaroita vuosikymmenien ajan.",
    [Key1, Typewriter, Muovipussi]
)
# |----------------------------------------------------------------------|



# |----------------------------------------------------------------------|
# Määritellään huoneiden väliset yhteydet
rooms = [entryway, kitchen, study, storage]

esineet = [Flashlight, Key1, Book, Typewriter, Muovipullo,
        Lasipurkki, Sanomalehti, Pahvilaatikko,Sailkepurkki, Paristo
        ]
roskat = [esine for esine in esineet if esine.onko_roska()] #Roskat sisältää vain esineet, joilla on jätelaji
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
#Pelin itse pääsilmukka

while True:
        show_menu()

        valinta = input("Valitse toiminto: ")

        if valinta == "1":  #Liiku valittuun huoneeseen
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

                    elif kohde == storage:
                        if not pelaaja.onko_esine("Taskulamppu"):
                            print(
                                "Varasto on liian pimeä. "
                                "Tarvitset taskulampun päästäksesi sisään."
                            )

                        elif not pelaaja.onko_esine("Paristo"):
                            print(
                                "Taskulamppu ei toimi ilman paristoa. "
                                "Sinun täytyy löytää paristo."
                            )

                        else:
                            pelaaja.liiku(kohde)

                    else:
                        pelaaja.liiku(kohde)

                else:
                    print("Virheellinen huonevalinta.")

            else:
                print("Anna numero.")

        elif valinta == "2":  #Kerää esineen
            pelaaja.take_item()

        elif valinta == "3":  #Näyttää pelaajan esineet
            print("\n-|- ESINEET -|-")

            if len(pelaaja.esineet) == 0:
                print("Sinulla ei ole esineitä.")
            else:
                for esine in pelaaja.esineet:
                    print(f"- {esine.nimi} ({esine.paino} kg)")

        elif valinta == "4":  #Näyttää nykyisen sijainnin
            print(f"\nOlet huoneessa: {pelaaja.sijainti.nimi}")
            print(pelaaja.sijainti.selite)

            if pelaaja.sijainti.esineet:
                print("\nHuoneessa on:")

                for esine in pelaaja.sijainti.esineet:
                    print(f"- {esine.nimi}")
            else:
                print("Huoneessa ei ole esineitä.")

        elif valinta == "5":  #Lajitellaan roskia
            lajittele_roskat(pelaaja)

            if len(pelaaja.lajitellut_roskat) == len(roskat):
                print("\n================================")
                print("         PELI PÄÄTTYI!")
                print("================================")

                print(
                    f"\nLajittelit oikein "
                    f"{pelaaja.pisteet}/{len(roskat)} roskaa."
                )

                if pelaaja.pisteet == len(roskat):
                    print(
                        "Täydellinen suoritus! "
                        "Kaikki roskat lajiteltiin oikein."
                    )

                elif pelaaja.pisteet >= len(roskat) / 2:
                    print(
                        "Hyvä työ! Suurin osa roskista "
                        "päätyi oikeaan paikkaan."
                    )

                else:
                    print(
                        "Aika paljon meni pieleen, "
                        "mutta ainakin yritit!"
                    )
                pelinum += 1 #Pelin päättyessä pelinum kasvaa yhdellä, jotta intro ja ohjeet eivät tulostu uudelleen turhaan
                tallenna_peli(pelaaja)
                break  #Lopetetaan peli

        elif valinta == "6":  #Näyttää pisteet
            print("\n-|- PISTEET -|-")

            lajiteltu = len(pelaaja.lajitellut_roskat)
            oikein = pelaaja.pisteet
            total = len(roskat)

            print(f"Lajiteltu: {lajiteltu}/{total}")
            print(f"Oikein: {oikein}/{total}")

        elif valinta == "0":  #Lopetetaan peli
            tallenna_peli(pelaaja)

            print("Peli lopetettu. Kiitos pelaamisesta!")
            break

        else:
            print(
                "Virheellinen valinta. "
                "Sinun pitää valita numero väliltä 0-6."
            )

        #Tallentaa pelin jokaisen toiminnon jälkeen
        tallenna_peli(pelaaja)

# |----------------------------------------------------------------------|

if __name__ == "__main__":
    main()