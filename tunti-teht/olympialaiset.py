vuosi = int(input("Anna olympialaisten vuosi (1896 tai uudempi): "))

while vuosi > 1895:
    if vuosi in (1916, 1940, 1944):
        print(vuosi, "- ei ole olympialaisten vuosi.")
    elif vuosi % 4 == 0 or vuosi == 2021:
        print(vuosi, "- on olympialaisten vuosi.")
    else:
        print(vuosi, "- ei ole olympialaisten vuosi.")
        
    vuosi = int(input("\nAnna olympialaisten vuosi (1896 tai uudempi)\nTai syötä numero alle tuon 1896 lopettaaksesi ohjelma: "))