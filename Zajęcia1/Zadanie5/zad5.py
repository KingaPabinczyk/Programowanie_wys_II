class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

    def info(self):
        return f"Telefon: {self.model}, producent: {self.producent}"


class Komunikacja:
    def wyslij_wiadomosc(self, odbiorca, tresc):
        return f"Wiadomość do {odbiorca}: '{tresc}' została wysłana."


class Rozrywka:
    def odtworz_muzyke(self, utwor):
        return f"Odtwarzanie utworu: {utwor}"


class Smartphone(Telefon):
    def __init__(self, model, producent):
        super().__init__(model, producent)
        self.komunikacja = Komunikacja()
        self.rozrywka = Rozrywka()

    def wyslij_wiadomosc(self, odbiorca, tresc):
        return self.komunikacja.wyslij_wiadomosc(odbiorca, tresc)

    def odtworz_muzyke(self, utwor):
        return self.rozrywka.odtworz_muzyke(utwor)


telefon = Smartphone("Galaxy S25", "Samsung")

print(telefon.info())
print(telefon.wyslij_wiadomosc("Jan", "Cześć!"))
print(telefon.odtworz_muzyke("Imagine Dragons - Believer"))
