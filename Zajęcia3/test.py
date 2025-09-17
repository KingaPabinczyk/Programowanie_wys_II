from geompy import figury2d, figury3d

print("Kwadrat: pole =", figury2d.pole_kwadratu(4), ", obwód =", figury2d.obwod_kwadratu(4))
print("Prostokąt: pole =", figury2d.pole_prostokata(3, 5), ", obwód =", figury2d.obwod_prostokata(3, 5))
print("Koło: pole =", figury2d.pole_kola(2), ", obwód =", figury2d.obwod_kola(2))

print("Sześcian: objętość =", figury3d.objetosc_szescianu(3), ", pole =", figury3d.pole_szescianu(3))
print("Prostopadłościan: objętość =", figury3d.objetosc_prostopadloscianu(2, 3, 4), ", pole =", figury3d.pole_prostopadloscianu(2, 3, 4))
print("Kula: objętość =", figury3d.objetosc_kuli(2), ", pole =", figury3d.pole_kuli(2))
