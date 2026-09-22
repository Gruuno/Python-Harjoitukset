import random

class Car:
    def __init__(self, registry_number, top_speed):
        self.registry_number = registry_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        #Arpoo jokaiselle autolle nopeuden muutoksen väliltä -10 ja +15 km/h
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.accelerate(nopeuden_muutos)
            auto.drive(1)

    def tulosta_tilanne(self):
        #Tulostaa selkeän otsikkorivi ja tauluko
        print(f"\nTilanne kilpailussa: {self.nimi}")
        print(f"{'Rekisteritunnus':<16} | {'Huippunopeus':<15} | {'Tämänhetkinen nopeus':<22} | {'Kuljettu matka':<15}")
        print("-" * 83)
        for auto in self.autot:
            print(f"{auto.registry_number:<16} | {auto.top_speed:<12} km/h | {auto.current_speed:<19} km/h | {auto.distance_traveled:<12} km |")
        print("-" * 83)

    def kilpailu_ohi(self):
        #Tarkistaa, onko mikään auto edes saavuttanut maalin
        for auto in self.autot:
            if auto.distance_traveled >= self.pituus_km:
                return True
        return False


#Pääohjelma
if __name__ == "__main__":
    #Luo kymmenen auton lista
    autolista = []
    for i in range(1, 11):
        rekisteri = f"| ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autolista.append(Car(rekisteri, huippunopeus))

    #Luo 8000 km kilpailun nimeltä "Suuri romuralli"
    romuralli = Kilpailu("Suuri romuralli", 8000, autolista)

    tunnit = 0
    
    #Simuloi kilpailun
    while not romuralli.kilpailu_ohi():
        romuralli.tunti_kuluu()
        tunnit += 1
        
        #Tulostaa tilanteen joka 10 tunnin välein
        if tunnit % 10 == 0:
            print(f"\nAikaa kulunut: {tunnit} tuntia")
            romuralli.tulosta_tilanne()

    #Tulostaa lopputilanteen kilpailun loputtua
    print(f"\nKilpailu ohi! Aikaa kului yhteensä {tunnit} tuntia.")
    romuralli.tulosta_tilanne()