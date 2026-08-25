Vastaus1 = float(input("Anna hemoglobiinisi arvo (g/dl): "))
Vastaus2 = str(input("Anna sukupuolesi (mies/nainen): "))

if Vastaus2 == "mies":
    if Vastaus1 >= 134 and Vastaus1 <= 195:
        print("Hemoglobiinisi on normaali.")
    elif Vastaus1 < 134:
        print("Hemoglobiinisi on alhainen.")
    elif Vastaus1 > 195:
        print("Hemoglobiinisi on korkea.")

if Vastaus2 == "nainen":
    if Vastaus1 >= 117 and Vastaus1 <= 175:
        print("Hemoglobiinisi on normaali.")
    elif Vastaus1 < 117:
        print("Hemoglobiinisi on alhainen.")
    elif Vastaus1 > 175:
        print("Hemoglobiinisi on korkea.")