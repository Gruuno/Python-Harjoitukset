nimet = set()

while True:
    nimi = input("Anna nimi! Voit lopettaa ohjelman painamalla enteriä: ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Nimi on jo listassa.")
    else:
        print("Syötit uuden nimen.")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)