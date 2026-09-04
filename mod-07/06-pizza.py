import math

def laske_yksikköhinta(halkaisija_cm, hinta_euroa):
    säde_m = (halkaisija_cm / 100) / 2

    pinta_ala_m2 = math.pi * (säde_m ** 2)

    yksikköhinta = hinta_euroa / pinta_ala_m2
    return yksikköhinta

def main():
    print("~~~ Pizza 1 ~~~")
    halkaisija1 = float(input("Anna 1. pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna 1. pizzan hinta (€): "))

    print("\n~~~ Pizza 2 ~~~")
    halkaisija2 = float(input("Anna 2. pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna 2. pizzan hinta (€): "))

    hinta_per_m2_pizza1 = laske_yksikköhinta(halkaisija1, hinta1)
    hinta_per_m2_pizza2 = laske_yksikköhinta(halkaisija2, hinta2)

    print(f"\n1. pizzan yksikköhinta: {hinta_per_m2_pizza1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta: {hinta_per_m2_pizza2:.2f} €/m²")

    if hinta_per_m2_pizza1 < hinta_per_m2_pizza2:
        print("\nPizza 1 antaa paremman vastineen rahalle!")
    elif hinta_per_m2_pizza2 < hinta_per_m2_pizza1:
        print("\nPizza 2 antaa paremman vastineen rahalle!")
    else:
        print("\nMolemmat pizzat ovat yhtä edullisia neliöhinnaltaan!")

main()