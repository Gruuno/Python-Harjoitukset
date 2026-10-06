backpack = []

#1. KUHAN PITUUS 'PELI'
def play_pike():
    print("\n--- Kuhan pituus ---")

    length = float(input("Anna kuhan pituus (cm): "))

    if length < 37:
        print("Kuhan pituus on liian lyhyt. Vapauta se.")
    else:
        print("Kuhan pituus on riittävä! Ei tarvitse vapauttaa.")
 

#2. TILAUS 'PELI'
def play_ordering():
    print("\n--- Tilaus ---")

    age = int(input("Anna ikäsi: "))

    species = input(
        "Anna lajisi:\n"
        "Laji valikko: ihminen, tonttu tai robotti: "
    ).strip().lower()

    if age < 18 and species == "ihminen":
        print("Saat tilata vain kahvin!")

    elif age >= 18 and species == "ihminen":
        print("Saat tilata kahvia, olutta tai viiniä!")

    elif age < 100 and species == "tonttu":
        print("Saat tilata vain kahvin!")

    elif age >= 100 and species == "tonttu":
        print("Saat tilata kahvia, viiniä tai olutta!")

    elif species == "robotti":
        print("Saat tilata vain öljyä tai kahvia!")

    else:
        print("Virheellinen laji.")


#3. LISÄÄ ESINEEN REPPUUN
def add_item():
    print("\n--- Kerää esine ---")

    item = input("Minkä esineen haluat lisätä reppuun? ")

    if item.strip():
        backpack.append(item)
        print(f"Hienoa! '{item}' lisättiin reppuun.")
    else:
        print("Et kirjoittanut mitään. Mitään ei lisätty.")


#4. NÄYTÄÄ REPUN SISÄLLÖN
def show_backpack():
    print("\n--- Repun sisältö ---")

    if not backpack:
        print("Reppusi on vielä tyhjä. Käy keräämässä esineitä!")

    else:
        print("Repustasi löytyy seuraavat esineet:")

        for i, item in enumerate(backpack, 1):
            print(f"{i}. {item}")




#OHJELMAN PÄÄOSIO

#Kysytään pelaajan nimi ja ikä
name = input("Anna pelaajan nimi: ")
age = int(input("Anna pelaajan ikä: "))


#Tarkistetaan pelaajan ikä
if age <= 12:
    print(f"\nPelaajan nimi on: {name} ja ikä on: {age} vuotta.")
    print(
        "Valitettavasti et ole tarpeeksi vanha pelaamaan. "
        "Pelaajan tulee olla vähintään 13-vuotias."
    )
    print("Ohjelma päättyy.")

else:
    print(f"\nPelaajan nimi on: {name} ja ikä on: {age} vuotta.")
    print("Tervetuloa pelaamaan!")

    #Päävalikko
    while True:
        print("\n=== PÄÄVALIKKO ===")
        print("1 = Pelaa peliä: Kuhan pituus")
        print("2 = Pelaa peliä: Tilaus")
        print("3 = Lisää esine reppuun")
        print("4 = Katso repun sisältö")
        print("Kirjoita 'lopeta' sulkeaksesi ohjelman.")

        answer = input("\nValitse toiminto: ").strip().lower()


        #1 = Kuhan pituus
        if answer == "1":
            play_pike()

        #2 = Tilaus
        elif answer == "2":
            play_ordering()

        #3 = Lisää esineen reppuun
        elif answer == "3":
            add_item()

        #4 = Katso repun sisältö
        elif answer == "4":
            show_backpack()

        #Lopettaa ohjelman
        elif answer == "lopeta":
            print("\nOhjelma lopetetaan. Kiitos pelaamisesta!")
            break
        else:
            print("Virheellinen syöte. Yritä uudelleen.")