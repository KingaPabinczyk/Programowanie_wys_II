import json

class AplikacjaMobilna:

    liczba_pobran = 0
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja
        self.nowe_pobranie()

    def nowe_pobranie(self):
        AplikacjaMobilna.liczba_pobran += 1

    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as f:
            text = json.load(f)
            nazwa = text['nazwa']
            wersja = text['wersja']
        return cls(nazwa, wersja)

    @classmethod
    def ile_pobran(cls):
        return AplikacjaMobilna.liczba_pobran


app = AplikacjaMobilna.z_json("app.json")
print(app.nazwa, app.wersja)
print(AplikacjaMobilna.ile_pobran())
app2 = AplikacjaMobilna("app1","2.3.1")
print(app2.nazwa, app2.wersja)
print(AplikacjaMobilna.ile_pobran())



