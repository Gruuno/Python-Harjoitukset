Vastaus1 = int(input("Anna vuosi: "))

if Vastaus1 % 4 == 0 and Vastaus1 % 100 != 0 or Vastaus1 % 400 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")