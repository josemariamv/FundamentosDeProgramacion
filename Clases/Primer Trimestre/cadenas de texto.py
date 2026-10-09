# Tenemos que ser precavidos con cuando usar el signo + y la coma
# Dentro de un print funciona cualquiera de ambas
# aunque de forma ligeramente diferente. El signo + concatena cadenas tal cual
# mientras que la coma introduce un separador que, por defecto, es un espacio en blanco
print("Esto", "es", "un mensaje")
print("Esto" + "es" + "un mensaje")

# Fuera de un print, en una asignación, el signo + funciona igual que dentro de un print
texto = "Esto" + "es" + "un mensaje"
print(texto)

# pero la coma no hace lo que tu te piensas fuera del print.
# no concatena textos: forma una lista.
# ya veremos que es esto mas adelante cuando veamos estructuras complejas de datos
texto = "Esto", "es", "un mensaje"
print (texto)

# Esto da error. Python no concatena números y textos como hace java
# cadena1 = "Estoy concatenando" + 3 + "cadenas" + "una detrás de otra"
# Tenemos que convertir a string el número para que funcione:
cadena1 = "Estoy concatenando " + str(3) + " cadenas" + " una detrás de otra"
print(cadena1)

# Sin embargo en un print con comas si que puedo hacerlo:
print("Estoy concatenando", 3, "cadenas", "una detrás de otra")

# Podemos hacer referencia a un caracter cualquiera de una cadena poniendo su posición con esta sintaxis:
texto = "Hola Mundo Cruel"
print(texto[2])
# Lo anterior muestra el caracter número 2 de la cadena que es la l
# recuerda que la primera posición es la 0

# Si el número es negativo empezamos por el final. La posición -1 es la última. Lo siguiente muestra la e
print(texto[-2])

# Los slices, rebanadas o bocadillos son uno de los elementos mas útiles de las cadenas de python
# Cuando ponemos dos números extrae la subcadena entre la posición del primer número, incluida
# y la del segundo no incluida. Lo siguiente mostraría las posiciones entre la 2 y la 4
print(texto[2:5])
# Si cualquiera de ambos números es negativo busca la posición por detrás.
print(texto[2:-5])
# Si omitimos el primer número considera que es el 0
print(texto[:6])
# Si omitimos el segundo, llega hasta el final de la cadena
print(texto[2:])
# Podemos incluir un tercer parámetro. Un paso. Lo siguiente imprime las posiciones pares de la cadena
print(texto[::2])
# Y lo siguiente las impares
print(texto[1::2])
# cuando el paso es negativo va restando posiciones.
# Además, si el paso es positivo y omitimos el primer parámetro considera que es desde el final
# y si omitimos el segundo, hasta el principio. Así, lo siguiente muestra el texto al revés
print(texto[::-1])

# La función len devuelve la longitud de la cadena.
print(len("Hola mundo!"))

# esto da error. No se puede modificar una cadena directamente
# texto[0] = "X"

# Vamos a ver ahora formas de recorrer una cadena caracter a caracter. La más fácil es esta:
for caracter in texto:
    print(caracter)

# O También podemos usar range. Mejora sobre el anterior que tenemos la posición del caracter y el caracter en si
for i in range(len(texto)):
    print(i, " - ", texto[i])

# Además, me permite jugar con los tres parámetros que tiene el range (inicio, fin y paso) que son muy parecidos a
# los de los slices. Repasa el tema de bucles si no te acuerdas
# Lo siguiente recorre la cadena al revés:
for i in range(len(texto)-1, -1, -1):
    print(i, " - ", texto[i])

# Tenemos aún otra forma, pero ya la estudiaremos mas adelante:
for i, letra in enumerate(texto):
    print("***", i, " - ", letra)

# Algunos métodos interesantes
# Los siguientes devuelven la cadena toda con mayúsculas, toda con minúsculas o inviritendo ambas
print(texto.upper())
print(texto.lower())
print(texto.swapcase())
# Ninguna de estas funciones modifica la cadena original. Solo me devuelven una nueva cadena. Si quiero
# modificar la original tengo que reasignarla
texto = texto.upper()

# find encuentra la primera posición donde se encuentra la subcadena indicada
print(texto.find("M"))
print(texto.find("UND"))

# Si no la encuentra devuelve -1
print(texto.find("x"))

# Podemos añadir dos parámetros start y end para buscar en una porción de la cadena
print(texto.find("O", 8))
print(texto.find("O", 8,len(texto)-1))

# count devuelve el número de veces que aparece la subcadena
print(texto.count("O"))

# replace sustituye todas las ocurrencias del primer argumento por el segundo
print(texto.replace("O", "***"))
print(texto.replace("OL", "*"))
print(texto.replace(" ", "-"))

# Podemos añadir un tercer parámetro con el número máximo de sustituciones a realizar
print(texto.replace("O", "xxx", 1))

#La cadena original sigue sin alterarse, recuérdalo!
print(texto)

# zfill llena con ceros a la izquierda hasta completar el tamaño que se pasa como argumento
# Útil para formatear números
codigo = "1345"
codigo = codigo.zfill(10)
print(codigo)

# si el número es igual o inferior al tamaño de la cadena no hace nada
codigo = codigo.zfill(3)
print(codigo)

# Por último, strip elimina los espacios en blanco a derecha e izquierda de la cadena
texto = "       Hola  mundo    "
print(texto.strip() + ".")

# rstrip elimina solo los espacios por la derecha y ltrip por la izquierda
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

# existen muchas otras funciones útiles de cadenas. Estos son solo unos ejemplos. Si descubres otras
# que te parecen útiles y no hemos visto compártelas con el resto de alumnos/as

