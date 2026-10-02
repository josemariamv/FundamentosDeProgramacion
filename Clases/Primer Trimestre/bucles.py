# bucle for
# Lo usamos cuando podemos cuantificar de antemano cuantas veces vamos a hacer la repetición
import random

for i in range(5):  # Empieza en el 0 y termina en el 4
    print(i)

print("###")
for i in range(2,5):  # Empieza en el 2 y termina en el 4
    print(i)

print("###")
for i in range(2,11,2):  # Empieza en el 2 y termina en el 10 y avanza de 2 en 2
    print(i)

print("###")
for i in range(5,2,-1):  # Empieza en el 5 y termina en el 3 contando hacia atrás
    print(i)

print("###")
for i in range(10,1,-2):  # Empieza en el 10 y termina en el 2 contando hacia atrás de dos en dos
    print(i)

print("###")
vocales="AEIOU"
for letra in vocales: # recorre caracter a caracter la cadena de texto
    print(letra)

# bucle while
# Lo utilizamos cuando no sabemos de antemano cuantas veces vamos a repetir, aunque también se puede usar
# ante una situación como la de un for

print("###")
contador = 0
while contador < 5: # equivalente al for in range(5) pero, como vemos, necesita mas andamiaje
    print(contador)
    contador += 1

# Un caso mas apropiado: terminamos cuando sale un 6
print("###")
dado = 0
while dado!=6:
    dado = random.randint(1,6)
    print(dado)

# en python no existe el bucle do while