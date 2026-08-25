Vastaus1 = float(input("Anna huoneen lämpötila (°C): "))

if Vastaus1 <= 0:
    print("Lämpötila on pakkasen puolella.")
else:
    if Vastaus1 <= -20:
        print("Lämpötila on erittäin kylmä.")
    else:
        if Vastaus1 > 0:
            print("Lämpötila on plussan puolella.")