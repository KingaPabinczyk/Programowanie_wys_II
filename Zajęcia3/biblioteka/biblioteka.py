"""
Biblioteka
"""
class Ksiazka:
    """Książka"""
    def __init__(self, tytul, autor, dostepna=True):
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna

    def __str__(self):
        status = "dostępna" if self.dostepna else "niedostępna"
        return f"'{self.tytul}' ({self.autor}) - {status}"

    def z(self):
        """Z"""
        return f"'{self.tytul}' ({self.autor})"


class Biblioteka:
    """Biblioteka"""
    def __init__(self):
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """Dodaj książkę"""
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """Wypożycz książkę"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                if ksiazka.dostepna:
                    ksiazka.dostepna = False
                    return f"Wypożyczono: {tytul}"
                return f"Książka '{tytul}' jest niedostępna"
        return f"Brak książki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """Zwróć książkę"""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrócono: {tytul}"
        return f"Nie należy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """Ks"""
        return [
            ksiazka.tytul
            for ksiazka in self.lista_ksiazek
            if ksiazka.dostepna
        ]


def main():
    """Przykład"""
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedźmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostępne książki:", biblioteka.dostepne_ksiazki())


if __name__ == "__main__":
    main()
