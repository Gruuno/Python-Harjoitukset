import random

arvottu_luku = random.randint(1, 10)

print("Tervetuloa arvauspeliin!")

while arvottu_luku != 0:
    vastaus = int(input("Arvaa luku väliltä 1-10: "))

    if vastaus == arvottu_luku:
        print("Arvauksesi", vastaus, "oli oikein!")
        break
    elif vastaus > arvottu_luku:
        print("Arvauksesi on liian suuri!")
    else:
        print("Arvauksesi on liian pieni!")