# para recibir datos desde teclado
edad = input("Dime tu edad: ")
# los datos del teclado se reciben siempre como textos. Cuando queremos operar con ellos debemos de convertirlos
# a numéricos. Además, debemos de comprobar antes que son correctos o provocarán excepciones

anyo = 2026
print("hola", "mundo")
print("hola"+"mundo")
# esto no funciona. en Java si!
# print("hola"+"mundo"+anyo)

#asi si funciona
print("hola", "mundo", "-", anyo)

# hablaremos mas de print. Por ahora solo saber que tiene dos parámetros que por defecto valen end="\n" y sep=' '
print("hola", "mundo", "-", anyo, end="")
print("hola", "mundo", anyo, sep=" - ")