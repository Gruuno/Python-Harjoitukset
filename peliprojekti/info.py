import runpy
name = input("Anna pelaajan nimi: ")
age = int(input("Anna pelaajan ikä: "))


while age > 12:
    print("\nPelaajan nimi on: " + name + " ja ikä on: " + str(age) + " vuotta.")
    print("\nTervetuloa pelaamaan!")
    answer = input("Mitä peliä haluat pelata? (1 = Kuhan pituus, 2 = Tilaus) \nVoit myös lopettaa pelin kirjoittamalla 'lopeta': ")
    if answer == "1":
        runpy.run_path("../Python-Harjoitukset-V1-AMK/mod-04/01-kuha.py")
    elif answer == "2":
        runpy.run_path("../Python-Harjoitukset-V1-AMK/tunti-teht/tilaus.py")
    elif answer == "lopeta":
        print("Ohjelma lopetetaan. Kiitos pelaamisesta!")
        break
    else:
        print("Virheellinen syöte. Yritä uudelleen.")

if age <= 12:
    print("Pelaajan nimi on: " + name + " ja ikä on: " + str(age) + " vuotta.")
    print("Valitettavasti et ole tarpeeksi vanha pelaamaan. Pelaajan tulee olla vähintään 13-vuotias.")
    print("Ohjelma päättyy.")
# sori jos tein hiukan liikaa tän kanssa, en ollut ihan varma miten pitkälle tän kanssa piti mennä.