class Auto:
    def __init__(self, Registery_Number, Top_Speed):
        self.Registery_Number = Registery_Number
        self.Top_Speed = Top_Speed
        self.Current_Speed = 0
        self.Distance_Traveled = 0


#Pääohjelma
if __name__ == "__main__":
    New_Car = Auto("ABC-123", 142)

    #Tulostaa auton ominaisuuksia
    print(f"Rekisteritunnus: {New_Car.Registery_Number}")
    print(f"Huippunopeus: {New_Car.Top_Speed} km/h")
    print(f"Tämänhetkinen nopeus: {New_Car.Current_Speed} km/h")
    print(f"Kuljettu matka: {New_Car.Distance_Traveled} km")
