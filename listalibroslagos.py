import os


def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

import os
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione enter para continuar")
limpiar();

def ya_hechos():
    pass
print(F'''{Fore.WHITE+ Style.BRIGHT + Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗    
    ║                               LIBRERIA                                      ║    
    ║                              "El Lector"                                    ║    
    ╚═════════════════════════════════════════════════════════════════════════════╝    {Style.RESET_ALL}''')


class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Puntuación: {self.puntuacion}'

# Lista para almacenar los libros
lista_libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", "Ficcion", 4.5),
    Libro("1984", "George orwell", "Ciencia Ficcion", 4.3),
    Libro("El Hobbit", "J.R.R Tolkien", "Fantasia", 4.7),
    Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2),
    Libro("Crimen y Castigo", "Fiodor Dostoyevski", "Clasico", 4.4),
    Libro("Los Juegos Del Hambre", "Suzanne Collins", "Juvenil", 4.1),
    Libro("Don Quijote De La Mancha", "Miguel de Cervantes", "Clasico", 4.6),
    Libro("Harry Potter y la Piedra Filosofal", "J.K Rowling", "Fantasia", 4.8),
    Libro("Los Pilares de la Tierra", "Ken Follet", "Historica", 4.4),
    Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasia", 4.0)
]


def consultar_libro(titulo):
    for libro in lista_libros:
        if libro.titulo.lower() == titulo.lower():
            return libro
    return None

def agregar_libro():     # Solicitar información al usuario
    
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    puntuacion = input("Ingrese la puntuación del libro (0-10): ")
    
    # Validar la puntuación
    while not (puntuacion.isdigit() and 1 <= int(puntuacion) <= 10):
        puntuacion = input("Ingrese la puntuación en números del 1 al 10: ")

    puntuacion = int(puntuacion)

    # Crear una instancia de Libro y agregarla a la lista
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)
    print("Libro agregado exitosamente.")

def eliminar_libro():
    # Eliminar libro
    titulo = input("Por favor, ingrese el título del libro que desea eliminar de la lista: ")
    libro = consultar_libro(titulo)
    if libro is not None:
        lista_libros.remove(libro)
        print(f"El libro '{titulo}' ha sido eliminado de la lista.")
    else:
        print(f"El libro '{titulo}' no existe en la lista.")
        respuesta = input("¿Desea agregar un libro a la lista? (s/n): ")
        if respuesta.lower() == 's':
            agregar_libro()
        elif respuesta.lower() == 'n':
            print("¡Hasta luego!")
        else:
            print("Respuesta inválida. Por favor, ingrese 's' o 'n'.")

def mostrar_libros():
    if not lista_libros:
        print("No hay libros guardados.")
    else:
        print("\nLibros guardados:")
        for libro in lista_libros:
            print(libro)

def mejor_libro_por_genero(genero):
    libros_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if not libros_genero:
        return None
    return max(libros_genero, key=lambda libro: libro.puntuacion)

nombre = input("\tBienvenido, por favor, decime tu nombre: ")
print(f"Hola {nombre}, bienvenido a la biblioteca de libros.")

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        print(f"\nLas opciones son:")

        print("Opcion --> 1. Agregar un libro a la lista")
        print("Opcion --> 2. Eliminar un libro de la lista")
        print("Opcion --> 3. Consultar libro de la lista")
        print("Opcion --> 4. Mostrar todos los libros que esten registrados")
        print("Opcion --> 5. Mostrar el mejor libro segun género y puntuacion")
        print("Opcion --> 6. Salir")
        opcion = input(f"{nombre}, por favor indica la opción que gustes: ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            eliminar_libro()
        elif opcion == '3':
            titulo_a_consultar = input(f"{nombre}, por favor, ingresa el título del libro que deseas consultar: ")
            libro_encontrado = consultar_libro(titulo_a_consultar)

            if libro_encontrado:
                print(libro_encontrado)
            else:
                print(f"{nombre}, lamentablemente, no encontramos el libro que buscas.")
        elif opcion == '4':
            mostrar_libros()
        elif opcion == '5':
            genero_favorito = input(f"{nombre}, por favor, ingresa tu género favorito para hacerte una recomendación: ")
            mejor_libro = mejor_libro_por_genero(genero_favorito)

            if mejor_libro:
                print(f"{nombre}, el mejor libro en el género '{genero_favorito}' es:")
                print(mejor_libro)
            else:
                print(f"{nombre}, lamentablemente no se encontraron libros en el género '{genero_favorito}'.")
        elif opcion == '6':
            print(f"Gracias {nombre}, vamos a salir del programa.")
            break
        else:
            print(f"{nombre}, la opcion no es correcta, Por favor, selecciona una opción válida...")