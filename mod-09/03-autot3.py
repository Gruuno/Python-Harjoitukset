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
    new_car = Car("ABC-123", 142)
    new_car.accelerate(60)  #Asetetaan nopeudeksi 60 km/h
    new_car.distance_traveled = 2000
    
    new_car.drive(1.5) #Ajoaika

    #Pitäisi tulostaa kuljettu matka ajon jälkeen
    print(f"Kuljettu matka ajon jälkeen: {new_car.distance_traveled} km")