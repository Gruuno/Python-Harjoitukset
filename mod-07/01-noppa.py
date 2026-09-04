import random

def DiceThrow():
    return random.randint(1, 6)

def Main():
    throw = 0
    
    while throw != 6:
        throw = DiceThrow()
        if throw == 6:
            print(f"Onneksi olkoon! Nopan heitoksi tuli: {throw}. Peli päättyy.")
        else:
            print(f"Nopan heitoksi tuli: {throw}, jatketaan heittämistä...")

Main()