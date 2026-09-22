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


class ElectricCar(Car):
    def __init__(self, registry_number, top_speed, battery_capacity):
        super().__init__(registry_number, top_speed)
        #Sähköautolle oma ominaisuus: akun kapasiteetti kilowattitunteina
        self.battery_capacity = battery_capacity


class CombustionEngineCar(Car):
    def __init__(self, registry_number, top_speed, tank_size):
        super().__init__(registry_number, top_speed)
        #Polttomoottoriautolle oma ominaisuus: tankin koko litroina
        self.tank_size = tank_size


#Pääohjelma
if __name__ == "__main__":
    #"Luodaan" sähköauto ja polttomoottoriauto
    sahkoauto = ElectricCar("ABC-15", 180, 52.5)
    bensauto = CombustionEngineCar("ACD-123", 165, 32.3)

    #Asettaa kummallekin autolle nopeuden
    sahkoauto.accelerate(100)
    bensauto.accelerate(120)

    #Asettaa kummallekin autolle ajomatkan ajan
    sahkoauto.drive(3)
    bensauto.drive(3)

    #Tulostaa autojen kuljettu matka
    print(f"Sähköauto ({sahkoauto.registry_number}) kulki: {sahkoauto.distance_traveled} km")
    print(f"Polttomoottoriauto ({bensauto.registry_number}) kulki: {bensauto.distance_traveled} km")