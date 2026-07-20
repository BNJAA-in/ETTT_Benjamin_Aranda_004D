def validar_titulo(titulo):
    if titulo.strip() != "":
        return True
    return False
def validar_autor(autor):
    if autor.strip() != "":
        return True
    return False
def validar_genero(autor):
    if autor.strip() != "":
        return True
    return False
def validar_año(año):
    if año > 0: 
        return True
    return False
def validar_editorial(editorial):
    if editorial.strip() != "":
        return True
    return False
def validar_es_novedad(novedad):
    if novedad.strip().upper() in ("S","N"):
        return True
    return False
def validar_codigo(codigo):
    if codigo.upper().strip() != "":
        return True
    return False
libros = {
'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
}
def precio_multa(multa):
    if multa > 0:
        return True
    return False
def validar_copias_disponibles(copias):
    if copias >= 0:
        return True
    return False
prestamos = {
'L001': [500, 4],
'L002': [700, 0],
'L003': [300, 10],
'L004': [400, 2],
'L005': [600, 1],
'L006': [350, 6],
}

def menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Copias por género
2. Búsqueda de libros por rango de multa
3. Actualizar multa de libro
4. Agregar libro
5. Eliminar libro
6. Salir
=====================================
""")

def leer_opcion():
    try:
        opc = int(input("Ingrese una opcion"))
    except ValueError:
        print("solo numeros enteros")
        return
    if opc >= 1 and opc <= 6:
        return opc
    else:
        print("solo numeros enteros")

def copias_genero(libros):
    total_stock = 0
    genero = input("Ingrese el genero del libro: ").lower()
    if validar_genero(genero) == False:
        print("El genero del libro no puede llevar espacios")
        return
    for codigo in libros:
        if libros [codigo][2] == genero:
            print(f"el nombre del libro es: {libros[codigo][0]}")
            total_stock += prestamos[codigo][1]
            print(f"El total de copias disponibles es:  {total_stock}")


def buscar_codigo(codigo):
    if codigo in libros:
        return True
    return False

def actualizar_multa(codigo,nueva_multa):
    if buscar_codigo == False:
        return False
    prestamos[codigo][0] = nueva_multa
    return True


def eliminar_libro(codigo):
    if buscar_codigo(codigo) == False:
        return False
    libros.pop(codigo)
    prestamos.pop(codigo)
    return True

def agregar_libro(codigo,titulo,autor,genero,año,editorial,es_novedad,precio_multa,copias_disponibles):
    codigo = input("Ingrese código del libro: ").upper()
    if validar_codigo(codigo) == False:
        print("El codigo no puede contener espacios en blanco")
        return
    titulo = input("Ingrese título:")
    if validar_titulo(titulo) == False:
        print("El titulo no puede contener espacios en blanco")
        return
    autor = input("Ingrese autor: ")
    if validar_autor(autor) == False:
        print("El autor del libro no puede contener espacios en blanco")
        return
    genero = input("Ingrese género: ")
    if validar_genero(genero) == False:
        print("El genero no puede contener espacios en blanco")
        return
    try: 
        año = int(input("Ingrese año de publicación:"))
    except ValueError:
        print("solo numeros enteros")
    else:
        if validar_año(año) == False:
            print("El año debe ser mayor a 0")
            return
    editorial = input("Ingrese editorial:")
    if validar_editorial(editorial) == False:
        print("La editorial no puede contener espacios en blanco")
        return
    es_novedad = input("¿Es novedad? (s/n)?:")
    if validar_es_novedad(es_novedad) == False:
        print("Caracter equivocado")
        return
    try:
        precio = int(input("Ingrese precio de multa: "))
    except ValueError:
        print("solo numeros enteros")
    else:
        if precio_multa(precio) == False:
            print("El precio multa debe ser mayor a 0")
            return
    try:
        copias_disponibles = int(input("ingrese copias disponibles: "))
    except ValueError:
        print("solo numeros enteros")
        return
    if validar_copias_disponibles(copias_disponibles) == False:
        print("El numero de copias debe ser mayor a 0")
        return
    libros.append(codigo,titulo,autor,genero,año,editorial,)
    prestamos.append(codigo,precio,copias_disponibles)


    

def main():
    while True:
        menu()
        op = leer_opcion()
        match op:
            case 1:
                print("===Copias por género===")
                copias_genero(libros)       
            case 2:
                print("===Búsqueda de libros por rango de multa===")

            case 3:
                while True:
                        print("===Actualizar multa de libro===")
                        codigo = input(("Ingrese código del libro:")).upper()
                        multa =int(input("Ingrese nueva multa: "))
                        if precio_multa(multa) == False:
                            print("la multa debe ser mayor a 0")
                            return
                        if buscar_codigo(codigo) == True:
                            print("Actualizado")
                            return
                        else:
                            print("El codigo no existe")
                            intentar = input("¿Desea actualizar otra multa (s/n)?: ").lower()
                            if intentar == "n":
                                break
            case 4:
                print("===Agregar libro===")
                if agregar_libro(codigo,titulo,autor,genero,año,editorial,es_novedad,precio_multa,copias_disponibles) == True:
                    print("Libro agregado")
            case 5:
                print("===Eliminar libro===")
                codigo = input("Ingrese el codigo del libro: ").upper()
                if eliminar_libro(codigo) == True:
                    print("Eliminado exitosamente")
                else:
                    print("El codigo no existe")
            case 6:
                print("Programa finalizado.")
                break
main()