class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin or kohde_kerros > self.ylin:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa.")
            return

        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.hissit = []
        
        #Luo halutun määrän hissejä
        for i in range(hissien_lukumäärä):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        #Tarkistaa, että annettu hissin indeksi on edes olemassa
        if hissin_numero < 0 or hissin_numero >= len(self.hissit):
            print(f"Hissiä numero {hissin_numero} ei ole olemassa.")
            return

        print(f"\nAjetaan hissiä numero {hissin_numero} kerrokseen {kohde_kerros}:")
        valittu_hissi = self.hissit[hissin_numero]
        valittu_hissi.siirry_kerrokseen(kohde_kerros)


#Pääohjelma
if __name__ == "__main__":
    #Luodaan "talo", jossa alin kerros 1, ylin kerros 7 ja 3 hissiä (indeksit 0, 1 ja 2)
    print("Luodaan talo (kerrokset 1-7, 3 hissiä)")
    talo = Talo(1, 7, 3)

    #Hissi 1 kerrokseen 5
    talo.aja_hissiä(0, 5)

    #Hissi 2 kerrokseen 3
    talo.aja_hissiä(1, 3)

    #Hissi 1 alimpaan kerrokseen
    talo.aja_hissiä(0, 1)