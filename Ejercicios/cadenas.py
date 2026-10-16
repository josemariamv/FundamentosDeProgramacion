# Ejercicios del boletín 5
# Importante: son todos ejercicios de validación que mejoraremos técnicamente cuando veamos expresiones regulares
# y excepciones. En este momento nos sirven para practicar condicionales y cadenas

# Validar un NIF
letrasValidas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cifrasValidas = "0123456789"
nif = input("Introduce tu nif: ")
if len(nif)!=9:
    print("Un nif tiene que tener exactamente 9 caractéres")
elif nif[-1] not in letrasValidas and nif[-1] not in letrasValidas.lower():
    print("El último caracter no es una letra")
else:
    correcto = True
    for caracter in nif[:-1]:
        if caracter not in cifrasValidas:
            correcto = False
    if correcto == False:
        print("Alguno de los ocho primeros dígitos no es un número")
    else:
        print("El nif es correcto")

# Validar NIF o NIE. Forma 1
letrasValidas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cifrasValidas = "0123456789"
letrasNIE = "XYZxyz"
nif = input("Introduce tu nif o nie: ")
if len(nif)!=9:
    print("Un nif o un nie tiene que tener exactamente 9 caractéres")
elif nif[-1] not in letrasValidas and nif[-1] not in letrasValidas.lower():
    print("El último caracter no es una letra")
else:
    correcto = True
    for caracter in nif[:-1]:
        if caracter not in cifrasValidas:
            correcto = False
    if correcto == False:
        if nif[0] in letrasNIE:
            correcto = True
            for caracter in nif[1:-1]:
                if caracter not in cifrasValidas:
                    correcto = False
            if correcto == True:
                print("Es un NIE válido")
            else:
                print("Alguno de los dígitos que debe de ser un número no lo es")
        else:
            print("Alguno de los dígitos que debe de ser un número no lo es")
    else:
        print("La entrada es un nif y es correcta")

# Validar NIF o NIE. Forma 2 usando isdigit()
letras="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
letrasNIE = "XYZxyz"
nif = input("Introduce tu nif o nie: ")
if len(nif) !=9:
    print("La longitud no es válida")
elif nif[-1] not in letras and nif[-1] not in letras.lower():
    print("El último caracter no es una letra")
else:
    if nif[:-1].isdigit():
        print("Es un nif correcto")
    elif nif[0] in letrasNIE and nif[1:8].isdigit():
        print("Es un nie corecto")
    else:
        print("No es un identificador correcto")

# Validación de formato de fechas DD/MM/YYYY
fecha = input("Introduce una fecha en formato DD/MM/YYYY: ")
if len(fecha) !=10:
    print("Formato ínvalido. La longitud no es correcta")
elif fecha[2]!="/" or fecha[5]!="/":
    print("Formato inválido. Falta alguna / o no están en su sitio")
else:
    dia = fecha[:2]
    mes = fecha[3:5]
    anno = fecha[6:]
    if dia.isdigit() and mes.isdigit() and anno.isdigit():
        dia = int(dia)
        mes = int(mes)
        anno = int(anno)
        if dia== 0 or dia > 31 or mes == 0 or mes > 12:
            print("El día o el mes no son válidos")
        else:
            if dia == 31 and (mes ==2 or mes==4 or mes==6 or mes == 9 or mes == 11):
                print("Ese mes no puede tener 31 días")
            elif mes == 2 and dia == 30:
                print("Febrero no puede tener 30 días")
            elif mes == 2 and dia == 29:
                if anno%4==0 and (anno%100!=0 or anno%400==0):
                    print("Fecha válida. Año bisiesto")
                else:
                    print("Febrero no puede tener 29 días si no es bisiesto")
            else:
                print("Fecha correcta")
    else:
        print("Formato inválido. Hay algún caracter incorrecto")