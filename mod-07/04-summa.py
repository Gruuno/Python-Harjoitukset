def laske_summa(lukulista):
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa

def main():
    luvut = []

    while True:
        luku = input("Anna luku (tyhjä lopettaa): ")

        if luku == "":
            break

        luvut.append(int(luku))

    kokonaissumma = laske_summa(luvut)

    print(f"\nSyötit luvut: {luvut}")
    print(f"Listassa olevien lukujen summa on: {kokonaissumma}")

main()