lentoasemat = {}

while True:
    toiminto = input("Syötä uusi lentoasema (uusi), hae lentoasema (haku) tai lopeta (lopeta): ")

    if toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ")
        print(lentoasemat[icao])

    elif toiminto == "lopeta":
        break