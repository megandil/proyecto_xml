def menu():
    print('''1.Mostrar el nombre de todos los videojuegos.
2.Muestra la cantidad de juegos pertenecientes a un genero introducido.
3.Busca el nombre de un juego y muestra las tiendas en las que se vende.
4.Muestra los juegos que tienen o no tienen ONLINE, dependiendo de la respuesta del usuario.
5.Muestra los juegos que sean compatibles con la plataforma de juego introducida.
6.Salir''')
    opcion=int(input("Introduce la opcion:"))
    return opcion
def leernombres():
    from lxml import etree
    doc = etree.parse('/home/usuario/Documentos/proyectolm/xml/proyecto_xml/videojuegos.xml')
    juegos=doc.xpath("//videojuego/titulo/text()")
    return juegos
def contargenero(nombregenero):
    from lxml import etree
    doc = etree.parse('/home/usuario/Documentos/proyectolm/xml/proyecto_xml/videojuegos.xml')
    generos=doc.xpath('//GENERO[@genero="%s"]/videojuego/titulo/text()' % nombregenero)
    cuenta=len(generos)
    return cuenta