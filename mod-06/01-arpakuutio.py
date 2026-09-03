import random

amount = int(input("Anna arpakuutioiden lukumäärä: "))

sum = 0

for i in range(amount):
    luku = random.randint(1, 6)
    sum += luku

print("Silmälukujen summa:", sum)