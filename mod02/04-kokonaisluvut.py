import math

Vastaus1 = int(input("Anna ensimmäinen kokonaislukusi: "))
Vastaus2 = int(input("Anna toinen kokonaislukusi: "))
vastaus3 = int(input("Anna kolmas kokonaislukusi: "))

Summa = Vastaus1 + Vastaus2 + vastaus3
Tulos = Vastaus1 * Vastaus2 * vastaus3
Keskiarvo = (Vastaus1 + Vastaus2 + vastaus3) / 3

print("Kokonaislukujesi summa on: " + str(Summa) + "!")
print("Kokonaislukujesi tulos on: ", f"{Tulos:.2f}!")
print("Kokonaislukujesi keskiarvo on: ", f"{Keskiarvo:.2f}!")