pienin = ""
suurin = ""

syote = input("Syötä luku (tyhjä lopettaa): ")

while syote != "":
    luku = float(syote)
    
    if pienin == "" or suurin == "":
        pienin = luku
        suurin = luku
    else:
        if luku < pienin:
            pienin = luku
        
        if luku > suurin:
            suurin = luku
            
    syote = input("Syötä luku (tyhjä lopettaa): ")

if pienin == "":
    print("Et syöttänyt yhtään lukua.")
else:
    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)