Vastaus1 = input("Maria oli rohkea ritari, joka joutui kaksintaisteluun. Minkä aseen Maria ottaa?\n")

while Vastaus1 != "lopeta":
    if Vastaus1 == "Miekka":
        print("Oikein voimakas ja urhea päätös! Harmittavasti vastaus on myös väärä. Koita uudelleen!")
        Vastaus1 = input("\nMinkä aseen Maria ottaa seuraavaksi? ")
        
    elif Vastaus1 == "Kilpi":
        print("Tykkäät suojella ystäviäsi? Kunnioittavaa. Vastauksesi on myös oikein.")
        Vastaus1 = "lopeta"
        
    elif Vastaus1 == "Sauva":
        print("Taikoja ja tulipalloja. Varo ympärystöäsi! Valitettavasti vastauksesi oli myös väärä. Koita uudelleen!")
        Vastaus1 = input("\nMinkä aseen Maria ottaa seuraavaksi? ")
        
    else:
        Vastaus1 = input("Syötit varmaankin väärän valinnan. Valintoina on Miekka, Kilpi tai Sauva!\n")

print("Ohjelma lopetetaan.")