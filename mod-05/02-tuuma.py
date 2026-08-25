tuumat = 0

while tuumat >= 0:
    tuumat = float(input("Anna tuumien lukumäärä (negatiivinen luku lopettaa laskelman): "))
    
    if tuumat >= 0:
        cm = tuumat * 2.54
        print(tuumat, "tuumaa on", cm, "cm")

print("Annoit negatiivisen luvun. Ohjelma lopetettu.")