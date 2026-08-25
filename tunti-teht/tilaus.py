Vastaus1 = int(input("Anna ikäsi: "))
Vastaus2 = str(input("Anna lajisi: \nLaji valikko: ihminen, tonttu tai robotti: "))

if Vastaus1 < 18 and Vastaus2 == "ihminen":
    print("Saat tilata vain kahvin!")
elif Vastaus1 >= 18 and Vastaus2 == "ihminen":
    print("Saat tilata kahvia, olutta tai viiniä!")

if Vastaus1 < 100 and Vastaus2 == "tonttu":
    print("Saat tilata vain kahvin!")
elif Vastaus1 >= 100 and Vastaus2 == "tonttu":
    print("Saat tilata kahvia, viiniä tai olutta!")

if Vastaus1 >= 0 and Vastaus2 == "robootti":
    print("Saat tilata vain öljyä tai kahvia!")