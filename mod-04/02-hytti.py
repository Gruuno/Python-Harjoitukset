Vastaus1 = str(input("Anna hyttisi luokka (A, B, C tai LUX): "))

if Vastaus1 == "A" or Vastaus1 == "a":
    print("Hyttisi 'A' on ikkunallinen ja sijaitsee autokannen yläpuolella.")
else:
    if Vastaus1 == "B" or Vastaus1 == "b":
        print("Hyttisi 'B' on ikkunaton ja sijaitsee autokannen yläpuolella.")
    else:
        if Vastaus1 == "C" or Vastaus1 == "c":
            print("Hyttisi 'C' on ikkunaton ja sijaitsee autokannen alapuolella.")
        else:
            if Vastaus1 == "LUX" or Vastaus1 == "lux":
                print("Hyttisi 'LUX' on parvekkeellinen ja sijaitsee yläkannen puolella.")
            elif Vastaus1 != "A" and Vastaus1 != "a" and Vastaus1 != "B" and Vastaus1 != "b" and Vastaus1 != "C" and Vastaus1 != "c" and Vastaus1 != "LUX" and Vastaus1 != "lux":
                print("Virheellinen hyttiluokka!")