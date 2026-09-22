class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
        print(self.nykyinen_kerros)

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
        print(self.nykyinen_kerros)

    def siirry_kerrokseen(self, kohde_kerros):
        #Rajojen ulkopuolelle meno esto
        if kohde_kerros < self.alin or kohde_kerros > self.ylin:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa.")
            return

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()


#Pääohjelma
if __name__ == "__main__":
    print("Luodaan hissi (alin kerros: 1, ylin kerros: 7)")
    h = Hissi(1, 7)

    print("\nSiirrytään kerrokseen 5:")
    h.siirry_kerrokseen(5)

    print("\nSiirrytään takaisin alimpaan kerrokseen (1):")
    h.siirry_kerrokseen(1)
