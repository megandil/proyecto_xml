from lxml import etree
from funciones import *
doc = etree.parse('/home/usuario/Documentos/proyectolm/xml/proyecto_xml/videojuegos.xml')
menus=menu()
print(menus)
while menus != 6:
    if menus == 1:
        for i in leernombres():
            print(i)
    if menus == 2:
        generos=doc.xpath('//GENERO/@genero')
        print("------------------------------")
        print("Los generos disponibles son:")
        print("------------------------------")
        for i in generos:
            print(i)
        genero=input("Introduce el género que quieres buscar: ")
        print("------------------CUENTA DE VIDEOJUEGOS-----------------------")
        print("Existen %i del género %s"% (contargenero(genero),genero))
        print("--------------------------------------------------------------")
    if menus == 3:
        menujuego=menujuegos()
        print(menujuego)
        while menujuego != 7:
            if menujuego == 1:
                juego="Valorant"
            if menujuego == 2:
                juego="FIFA 20"
            if menujuego == 3:
                juego="Minecraft"
            if menujuego == 4:
                juego="Final Fantasy VII"
            if menujuego == 5:
                juego="Mario Kart 8 Deluxe"
            if menujuego == 6:
                juego=input("Introduce el nombre del juego que quieres buscar: ")
            print("----Tiendas----")
            for i in tiendasjuego(juego):
                print("- ",i)
            print()
            menujuego=menujuegos()
            print(menujuego)
    menus=menu()
    print(menus)