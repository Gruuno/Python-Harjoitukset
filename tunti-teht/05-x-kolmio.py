korkeus = int(input("Anna kolmion korkeus!: "))

rivi = 1

while rivi <= korkeus:
    välilyönnit = korkeus - rivi
    tähdet = 2 * rivi - 1

    print(" " * välilyönnit + "*" * tähdet)

    rivi += 1 