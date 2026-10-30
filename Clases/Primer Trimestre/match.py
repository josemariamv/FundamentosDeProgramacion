# match es una instrucción condicional que me permite evaluar el valor en una variable y elegir entre diferentes
# opciones según dicho valor. En determinadas circunstancias me permite sustituir a una cadena de if-else
# haciendo mas legible el código. Por ejemplo en menús extensos

opcion = input("Escribe P para jugar, C para configurar o X para salir: ")
match opcion:
    case "P":
        print("Has elegido jugar")
    case "C":
        print("Has elegido configurar")
    case "X":
        print("Has elegido salir. Adios, hasta la próxima")

# Si queremos que se ejecute una opción por defecto, cuando la variable no cuadre con ninguno de los valores del match,
# usamos un case _:
# Esta opción, si aparece, debe de ser siempre la última
opcion = input("Escribe P para jugar, C para configurar o X para salir: ")
match opcion:
    case "P":
        print("Has elegido jugar")
    case "C":
        print("Has elegido configurar")
    case "X":
        print("Has elegido salir. Adios, hasta la próxima")
    case _:
        print("Opción incorrecta")

# Podemos hacer que haya múltiples valores que concuerden con el mismo bloque del case con este formato:
opcion = input("Escribe P para jugar, C para configurar o X para salir: ")
match opcion:
    case "P" | "p":
        print("Has elegido jugar")
    case "C" | "c":
        print("Has elegido configurar")
    case "X" | "x":
        print("Has elegido salir. Adios, hasta la próxima")
    case _:
        print("Opción incorrecta")