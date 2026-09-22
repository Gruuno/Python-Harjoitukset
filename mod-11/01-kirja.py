class Publish:
    def __init__(self, nimi):
        self.name = nimi


class Book(Publish):
    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages

    def print_info(self):
        print(f"Kirja: {self.name}")
        print(f"Kirjoittaja: {self.writer}")
        print(f"Sivumäärä: {self.pages} sivua")
        print()


class Magazine(Publish):
    def __init__(self, name, publisher):
        super().__init__(name)
        self.publisher = publisher

    def print_info(self):
        print(f"Lehti: {self.name}")
        print(f"Päätoimittaja: {self.publisher}")
        print()


#Pääohjelma
if __name__ == "__main__":
    magazine = Magazine("Aku Ankka", "Aki Hyyppä")
    book = Book("Hytti n:o 6", "Rosa Liksom", 200)

    magazine.print_info()
    book.print_info()