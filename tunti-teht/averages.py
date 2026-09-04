def averages(luvut):
    if not luvut:
        return 0.0
    return sum(luvut) / len(luvut)

maara = int(input("Kuinka monta numeroa syötät? "))
numerot = []

for i in range(maara):
    luku = int(input("Syötä luku: "))
    numerot.append(luku)

keskiarvo = averages(numerot)
print(f"Syötettyjen lukujen keskiarvo on: {keskiarvo:.2f}")