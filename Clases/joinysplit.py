# split y join son dos funciones muy útiles que realizan operaciones inversas
# split convierte una cadena en una lista de cadenas
# join convierte una lista de cadenas en una sola cadena

cadena = "a-b-c"
print(cadena.split("-"))

# sin argumentos, el separador por defecto es el espacio en blanco
# tantos como hubiera, no solo uno
# e ignora los espacios por delante y por detras (no hace falta usar strip previo)
# si hubiera tabuladores y saltos de línea también los obvia
cadena = ("      a  b    c\n")
print(cadena.split())

# podemos indicar un segundo parámetro que define el máximo número de cortes. El resto se obvia
cadena = "a, b, c, d, e, f"
print(cadena.split(", ", 3))

# rsplit corta por la derecha. Solo da valores diferentes si especificamos un número máximo de cortes
print(cadena.rsplit(", ", 3))

# splitlines separa por lineas (igual que split poniendo \n como separador)
cadena = "a\nb, c\nd\ne"
print(cadena.splitlines())

# partition lleva como argumento un separador y siempre devuelve tres partes: lo de antes, el separador y lo de después
cadena = "iesgoya.com"
print(cadena.partition("."))

# vamos con join. Unos ejemplos
separador = "-"
print(separador.join(["a", "b", "c"]))
print("".join(["a", "b", "c"]))
print("\n   ".join(["a", "b", "c"]))

# si se aplica sobre una cadena trata cada caracter como un elemento
print("*".join("abc"))

# si quiseramos usarla con números tenemos que convertirlos antes a textos
numeros = [1, 2, 3, 4, 5]
print(", ".join(str(n) for n in numeros))   # '1,2,3'

# juntos son muy útiles. Se puede invertir el orden de las palabras
frase = "yo quiero aprender python"
print(" ".join(frase.split()[::-1]))

# se puede capitalizar cada palabra de una frase
titulo = "el señor de los anillos"
print(" ".join(p.capitalize() for p in titulo.split()))

# normalizar el esceso de espacios
sucio = "  voy    a  borrar     todos    los    espacios   sobrantes     "
print(" ".join(sucio.split()))

# cambiar el formato de una fecha
fecha = "2026-10-15"
print("/".join(fecha.split("-")[::-1]))

# contar palabras
texto = "to be or not to be"
print(len(texto.split()))

# crear un slug para una URL de forma automática a partir de un título
titulo = "Mi Primer Artículo en Python"
slug = "-".join(titulo.lower().split())
print(slug)
