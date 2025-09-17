import math

def pole_kwadratu(a: float) -> float:
    return a * a

def obwod_kwadratu(a: float) -> float:
    return 4 * a

def pole_prostokata(a: float, b: float) -> float:
    return a * b

def obwod_prostokata(a: float, b: float) -> float:
    return 2 * (a + b)

def pole_kola(r: float) -> float:
    return math.pi * r**2

def obwod_kola(r: float) -> float:
    return 2 * math.pi * r
