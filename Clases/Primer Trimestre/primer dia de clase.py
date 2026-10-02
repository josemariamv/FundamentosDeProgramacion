
""" Esto es un comentario de
bloque
"""

print("hola mundo") # Esto es un comentario hasta el final de la línea
# En python no se definen variables. Tampoco se indica el tipo
edad = 5
precio = 10.5
texto = "Hola mundo"
acertado = False

# Si redefines una variable a otro tipo diferente cuela

texto = 57
print(texto)

#si trato de hacer algunas operaciones con una variable no definida previamente da error
# print(iva)
# cociente = dividendo / divisor

# En python no hay constantes, pero por convención se usan variables
# escritas con mayúsculas
MESES_DEL_ANNO = 12
#Pero, ojo, es una convención, no es una constante real. ¡Sigue siendo una variable!!!
MESES_DEL_ANNO = 11

# las asignaciones siempre tienen la menor prioridad en una instrucción
# y siempre se asigna de izquierda a derecha y nunca al revés
edad = edad + 1
print(edad)

# Los operadores de autoincremento y autodecremento no existen
#edad++

# el formato compacto cuando la misma variable está involucrada a derecha e izquierda del signo igual si
edad+=1

print(5/2)
print(5%2)
# este no lo hay en java. Nos da el cociente de la division entera
print(5//2)

#algunos operadores que no existen en java
potencia = 4 ** 2
print(potencia)
# también así
print(4**2)

# para la raiz necesitamos usar una función, como en java:
import math
numero = 49
raiz = math.sqrt(numero)
print(raiz)

#El operador + está sobrecargado para sumar cadenas
texto = "hola" + " " + "mundo"
print(texto)
# Tamién hay otros operadores sobrecargados... Algunos son utiles y otros no:
separador = "=" * 30
print(separador)

# El método print permite varios elementos separados por comas.
# Los muestra todos ellos usando un espacio en blanco como separador
# Ya veremos que es mucho mas flexible
nombre = "José María"
edad = 57
print("Hola mundo. Me llamo", nombre, "y tengo", edad, "años")

