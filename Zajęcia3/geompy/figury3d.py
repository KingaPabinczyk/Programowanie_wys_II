import math

def objetosc_szescianu(a: float) -> float:
    return a**3

def pole_szescianu(a: float) -> float:
    return 6 * a * a

def objetosc_prostopadloscianu(a: float, b: float, h: float) -> float:
    return a * b * h

def pole_prostopadloscianu(a: float, b: float, h: float) -> float:
    return 2 * (a*b + a*h + b*h)

def objetosc_kuli(r: float) -> float:
    return (4/3) * math.pi * r**3

def pole_kuli(r: float) -> float:
    return 4 * math.pi * r**2
