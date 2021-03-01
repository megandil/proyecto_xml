from lxml import etree
from funciones import *
doc = etree.parse('/home/usuario/Documentos/proyectolm/xml/proyecto_xml/videojuegos.xml')
menus=menu()
print(menus)
while menus != 6:
    if menus == 1:
        for i in leernombres():
            print(i)
    menus=menu()
    print(menus)