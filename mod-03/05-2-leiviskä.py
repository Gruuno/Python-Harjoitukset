while True:
    vastaus1 = float(input("Anna grammojen määrä (0 lopettaa): "))

    if vastaus1 == 0:
        print("Kiitos ohjelman käytöstä!")
        break

    elif vastaus1 < 0:
        print("Anna positiivinen luku")

    else:
        luoti = vastaus1 / 13.3
        naula = luoti / 32
        leiviska = naula / 20

        print(f"Leivisköitä: {leiviska:.2f}, Nauloja: {naula:.2f}, Luoteja: {luoti:.2f}")
