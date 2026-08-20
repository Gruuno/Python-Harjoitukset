import math

Vastaus1 = float(input("Kuinka monta leiviskää?: "))
Vastaus2 = float(input("Kuinka monta naulaa?: "))
vastaus3 = float(input("Kuinka monta luotia?: "))

luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

kokonaispaino_grammoina = Vastaus1 * leiviska + Vastaus2 * naula + vastaus3 * luoti
kilogrammat = float(kokonaispaino_grammoina / 1000)
grammat = kokonaispaino_grammoina - (kilogrammat * 1000)

print(f"Nykyajan mittojen mukaan paino olisi: {kilogrammat} kg ja {grammat:.2f} grammaa.")