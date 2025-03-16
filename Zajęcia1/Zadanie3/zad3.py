class Osoba:
    def __init__(self, imię, nazwisko, wiek):
        self.imię = str(imię)
        self.nazwisko = str(nazwisko)
        self.wiek = int(wiek)

    def przedstaw_się(self):
        return "Jestem "+self.imię + " " + self.nazwisko

class Pracownik(Osoba):
    def __init__(self, imię, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imię, nazwisko, wiek)
        self.stanowisko = str(stanowisko)
        self.pensja = float(pensja)

    def info_o_pracy(self):
        return "Pracuję jako " + self.stanowisko + ", zarabiam " + f" {self.pensja}" + " zł."

class Manager(Pracownik):
    zespół = []
    def __init__(self, imię, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imię, nazwisko, wiek, stanowisko, pensja)

    def dodaj_do_zespołu(self, pracownik):
        Manager.zespół.append(pracownik)
    def info_o_pracy(self):
        return ("Pracuję jako " + self.stanowisko + ", zarabiam "+ f" {self.pensja}" + " zł." + list(zespół) )


# os1 = Osoba("Kinga", "P", 25)
#
# print(os1.przedstaw_się())

pracownik = Pracownik("F","P",20,"pracownik",2)
manager = Manager("Kinga", "P",25,"manager",3)

manager.dodaj_do_zespołu(pracownik)
print(manager.info_o_pracy())