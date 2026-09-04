def karsi_parittomat(lukulista):
    parilliset = []
    for luku in lukulista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

def main():
    luvut = []

    while True:
        luku = input("Anna luku (tyhjä lopettaa): ")

        if luku == "":
            break

        luvut.append(int(luku))

    vain_parilliset = karsi_parittomat(luvut)

    print(f"\nAlkuperäinen lista: {luvut}")
    print(f"Karsittu lista (vain parilliset): {vain_parilliset}")

main()