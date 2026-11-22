# El operador ternario es la forma abreviada de una condicional binaria
# en una sola línea elige entre dos valores según una condición
# y ese valor se guarda en una variable o se usa dentro de otra instrucción
# Se llama ternario porque tiene tres partes:
# la condición, el valor si es verdadera y el valor si es falsa.

edad = 15

resultado = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(resultado)

# sería equivalente a
if edad >= 18:
    resultado = "Eres mayor de edad"
else:
    resultado = "Eres menor de edad"
print(resultado)

# lo más cómodo es la posibilidad de usarlo dentro de otra instrucción:
print("Eres mayor de edad" if edad >= 18 else "Eres menor de edad")

# Las condicionales de este tipo se pueden anidar como un if else pero
# en ese caso se vuelven tan complejas que no dejan de merecer la pena