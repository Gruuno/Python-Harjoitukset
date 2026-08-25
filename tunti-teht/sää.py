Vastaus1 = float(input("Anna sään lämpötila (°C): "))
Vastaus2 = str(input("Anna sään tila (aurinkoinen, pilvinen, sateinen): "))


if Vastaus1 <= 0:
    lampotila_teksti = "Lämpötila on pakkasen puolella"
elif Vastaus1 > 20:
    lampotila_teksti = "Lämpötila on lämmin!"
else:
    lampotila_teksti = "Lämpötila on tavallinen"


if Vastaus2 == "sateinen":
    saa_teksti = "Sää on sateinen."
elif Vastaus2 == "aurinkoinen":
    saa_teksti = "Sää on aurinkoinen."
elif Vastaus2 == "pilvinen":
    saa_teksti = "Sää on pilvinen."
else:
    saa_teksti = "Antamasi sää oli virheellinen."

print(lampotila_teksti, saa_teksti, "\nAnnoit arvot:", Vastaus2, "ja", Vastaus1)