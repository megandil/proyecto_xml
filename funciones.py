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
def tiendasjuego(nombrejuego):
    from lxml import etree
    doc = etree.parse('/home/usuario/Documentos/proyectolm/xml/proyecto_xml/videojuegos.xml')
    tiendas=doc.xpath('//GENERO/videojuego/titulo[text()="%s"]/../tiendas/tienda/text()' % nombrejuego)
    return tiendas
def menujuegos():
    print("------JUEGOS------")
    print('''1.Valorant (FPS)
2.Fifa 20 (Deportes)
3.Minecraft (Plataformas)
4.Final Fantasy VII Remake (RPG)
5.Mario Kart 8 Deluxe (Carreras)
6.Elegir otro
7.Salir''')
    opcion=int(input("Introduce la opcion:"))
    return opcion