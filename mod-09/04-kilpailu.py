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


#Pääohjelma
if __name__ == "__main__":
    #Luo listan autoista
    cars = []
    for i in range(1, 11):
        #Arvotaan satunnainen huippunopeus väliltä 100 - 200 km/h
        random_top_speed = random.randint(100, 200)
        #Luodaan uusi auto ja lisätään se listaan
        cars.append(Car(f"ABC-{i}", random_top_speed))

    race_ongoing = True
    hours_passed = 0

    #Itse kilpailun simulaatio
    while race_ongoing:
        hours_passed += 1
        
        for car in cars:
            #Arvotaan nopeuden muutos väliltä -10 - 15 km/h
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            
            #Määrittää ajettavan matkan ajan perusteella (1 tunti)
            car.drive(1)
            
            #Tarkistaa onko auto kulkenut tuon 10000 km
            if car.distance_traveled >= 10000:
                race_ongoing = False

    #Tulostaa kilpailun tulokset
    print(f"\n Kilpailu päättyi! Aikaa kului {hours_passed} tuntia.")
    print("-" * 68)
    print(f"| {'Rekisteri':<12} | {'Huippunopeus':<13} | {'Nykyinen nopeus':<16} | {'Kuljettu matka':<15}|")
    print("-" * 68)
    
    for car in cars:
        print(f"| {car.registry_number:<12} |  {car.top_speed:<8} km/h |  {car.current_speed:<11} km/h | {car.distance_traveled:<9.1f} km |")
    print("-" * 68)