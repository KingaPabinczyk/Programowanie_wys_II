class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = str(tytul)
        self.autor = str(autor)
        self.rok_wydania = int(rok_wydania)

    def opis(self):
        return f"'{self.tytul}' autorstwa {self.autor}, rok wydania: {self.rok_wydania}."


class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = float(rozmiar_pliku)

    def opis(self):
        return (super().opis() +
                f" Ebook (rozmiar pliku: {self.rozmiar_pliku:.2f} MB).")


class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = int(czas_trwania)

    def opis(self):
        return (super().opis() +
                f" Audiobook (czas trwania: {self.czas_trwania} minut).")


ebook1 = Ebook("Pan Tadeusz", "Adam Mickiewicz", 1834, 2.5)
ebook2 = Ebook("Lalka", "Bolesław Prus", 1890, 5.8)

audiobook1 = Audiobook("Quo Vadis", "Henryk Sienkiewicz", 1896, 720)
audiobook2 = Audiobook("Wiedźmin", "Andrzej Sapkowski", 1990, 540)

ksiazki = [ebook1, ebook2, audiobook1, audiobook2]

for ksiazka in ksiazki:
    print(ksiazka.opis())
