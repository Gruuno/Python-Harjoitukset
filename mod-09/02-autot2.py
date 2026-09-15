class Car:
    def __init__(self, registry_number, top_speed):
        self.registry_number = registry_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        #Laske uuden nopeude
        new_speed = self.current_speed + speed_change
        
        #Varmistaa, ettei nopeus ole yli huippunopeuden tai alle nolla
        if new_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed


#Pääohjelma
if __name__ == "__main__":
    new_car = Car("ABC-123", 142)

    #Nostaa nopeutta kolmessa vaiheessa
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)
    
    #Tulostaa kiihdytysten jälkeen oleva nopeus
    print(f"Nopeus kiihdytysten jälkeen: {new_car.current_speed} km/h")
    
    #Hätä jarrut
    new_car.accelerate(-200)
    
    #Tulostaa hätäjarrutuksen jälkeen oleva nopeus
    print(f"Nopeus hätäjarrutuksen jälkeen: {new_car.current_speed} km/h")