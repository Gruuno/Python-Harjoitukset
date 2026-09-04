def gallons(gallons):
    liters = gallons * 3.785
    return liters

def main():
    while True:
        feed = float(input("Anna bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))

        if feed <= 0:
            print("Ohjelma lopetetaan.")
            break

        in_liters = gallons(feed)

        print(f"{feed} gallonaa on {in_liters:.2f} litraa.\n")

main()