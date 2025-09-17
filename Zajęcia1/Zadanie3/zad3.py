class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = str(imie)
        self.nazwisko = str(nazwisko)
        self.wiek = int(wiek)

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}."


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = str(stanowisko)
        self.pensja = float(pensja)

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja:.2f} zł."


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = [] 

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}, mam {len(self.zespol)} podwładnych."

    def dodaj_do_zespolu(self, pracownik):
        if isinstance(pracownik, Pracownik):
            self.zespol.append(pracownik)
        else:
            raise TypeError("Do zespołu można dodać tylko pracownika.")


pracownik1 = Pracownik("Jan", "Kowalski", 30, "Programista", 5000)
pracownik2 = Pracownik("Anna", "Nowak", 28, "Tester", 4000)
manager = Manager("Kinga", "Pawlak", 35, "Manager", 8000)

manager.dodaj_do_zespolu(pracownik1)
manager.dodaj_do_zespolu(pracownik2)

print(pracownik1.przedstaw_sie())
print(pracownik1.info_o_pracy())
print(manager.przedstaw_sie())
print(manager.info_o_pracy())
