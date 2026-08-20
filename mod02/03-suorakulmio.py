import math

Vastaus1 = float(input("Anna suorakulmiosi kanta (cm): "))
Vastaus2 = float(input("Anna suorakulmiosi korkeus (cm): "))

Pinta_ala = Vastaus1 * Vastaus2
Piiri = 2 * (Vastaus1 + Vastaus2)

print("Suorakulmiosi pinta-alana on: ", f"{Pinta_ala:.2f} cm²!")
print("Suorakulmiosi piirinä on: ", f"{Piiri:.2f} cm!")