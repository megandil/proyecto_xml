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
    menus=menu()
    print(menus)