# condicional if

# Los operadores para comparar son los mismos que en cualquier lenguaje: <, >, <=, >=, == y !=
# Una condición tiene que evaluarse como verdad (True) o falso (False). No vale ninguna otra cosa

n = 128

if n > 100:
    print("mayor que 100")

# operadores especiales que no encontramos en otros lenguajes:

letra = "A"
if letra in "UOIAE":
    print("Es una vocal mayúscula")
else:
    print("No es una vocal mayúscula")

# debajo del if (o del else) abrimos un bloque (con tabulado) y debe de haber una instrucción mínimo
# pero puede haber tantas como queramos

if letra !="E":
    print("No es una E")
    print("Puede se cualquier otra cosa")

# como en cualquier bloque, si queremos dejarlo sin contenido podemos usar pass

letra="E"
if letra !="E":
    pass
else:
    print("Tiene que ser una E")

# Podemos hacer condiciones mas complejas combinando con "or" y/o con "and"

if letra !="E" and letra !="U":
    print("No es ni una E ni una U")

# OJO: no confundir = de asignación con == de comparación
if letra =="A" or letra =="I":
    print("Puede ser una A o una I")

# si tenemos dudas y la condición es compleja podemos agrupar con paréntesis
letra="O"
if (letra in ("AEIOU") and letra!="E") or letra=="X":
    print("Puede ser una vocal que no sea la E o una X")

# Usar elif reduce la confusión de los bloques de indentaciones en un if-else con mucha profundidad
if letra == "U":
    print("Es una U")
elif letra == "O":
    print("Es una O")
elif letra =="I":
    print("Es una I")
else:
    print("No es ni una U, ni una O, ni una I")

if n in range(0,255):
    print("en el rango adecuado")

n = 300
if n not in range(0,255):
    print("no está en el rango adecuado")

# cuidado con los rangos: el primer valor está incluido (0) pero el último no (255)
n = 255
if n not in range(0,255):
    print("no está en el rango adecuado")

# Podemos poner un if en úna única línea. Resta claridad a cambio de acortar el código
# solo recomendable si sabemos lo que hacemos
a = 2
if a > 5: print("Es mayor que 5")

if a > 5: print("Es mayor que 5"); print("Por tanto también es mayor que 4")
else: print("No es mayor que 5")

# Operador ternario
# Es un if simplificado. Sólo usarlo si lo entendemos bien
# Estructura:
# [código si se cumple] if [condición] else [código si no se cumple]
x = 5
print("Es 5" if x == 5 else "No es 5")
# El operador ternario no se puede usar sin else. Ni siquiera poniendo un pass el el bloque else