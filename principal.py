from lxml import etree
from funciones import *
doc = etree.parse('/home/usuario/Documentos/proyectolm/xml/proyecto_xml/videojuegos.xml')
#Sin la ruta completa en el "etree.parse" no me encuentra el fichero XML, por eso está puesta la ruta completa.
menus=menu()
print(menus)
while menus != 6:
    if menus == 1:
        print("------JUEGOS------")
        for i in leernombres():
            print("-",i)
        print()
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
    if menus == 4:
        onlines=input("¿Quieres ver juegos con ONLINE o sin ONLINE? Sin/Con: ")
        while onlines.upper() != "SIN" and onlines.upper() != "CON":
            print("No es una respuesta válida.")
            onlines=input("¿Quieres ver juegos con ONLINE o sin ONLINE? Sin/Con")
        if onlines.upper() == "CON":
            onlines="Si"
        if onlines.upper()== "SIN":
            onlines="No"
        print("------JUEGOS------")
        for i in online(onlines):
            print("-",i)
        print()
    if menus == 5:
        menuplataforma=menuplataformas()
        print(menuplataforma)
        while menuplataforma != 10:
            if menuplataforma == 1:
                plat="Playstation 5"
            if menuplataforma== 2:
                plat="Playstation 4"
            if menuplataforma == 3:
                plat="PS3"
            if menuplataforma == 4:
                plat="PC"
            if menuplataforma == 5:
                plat="Nintendo DS"
            if menuplataforma == 6:
                plat="Nintendo Switch"
            if menuplataforma == 7:
                plat="XBOX ONE"
            if menuplataforma == 8:
                plat="XBOX 360"
            if menuplataforma == 9:
                plat="Movil"
            print("------JUEGOS------")
            for i in juegosplataforma(plat):
                print("-",i)
            print()
            menuplataforma=menuplataformas()
            print(menuplataforma)
    menus=menu()
    print(menus)