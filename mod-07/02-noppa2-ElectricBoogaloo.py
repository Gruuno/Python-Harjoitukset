import random

def DiceThrow(sides):
    return random.randint(1, sides)

def Main():
    max = int(input("Anna nopan maksimiluku: "))

    throw = 0
    
    while throw != max:
        throw = DiceThrow(max)
        
        if throw == max:
            print(f"Onneksi olkoon! Nopan heitoksi tuli: {throw}. Peli päättyy.")
        else:
            print(f"Nopan heitoksi tuli: {throw}, jatketaan heittämistä...")

Main()