# condicional if
n = 128

if n > 100:
    print("mayor que 100")

letra = "A"
if letra in "UOIAE":
    print("Es una vocal mayúscula")
else:
    print("No es una vocal mayúscula")

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