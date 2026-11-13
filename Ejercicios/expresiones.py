import re
'''
# el de comprobar si es un NIF o un NIE válido
patronNIE = r"[XYZ][0-9]{7}[A-HJ-NP-TV-Z]?"
patronNIF = r"[0-9]{8}[A-HJ-NP-TV-Z]?"
cadena = "Y8398414T"

if re.fullmatch(patronNIF, cadena) or re.fullmatch(patronNIE, cadena):
    print(cadena, "es un identificador válido")
else:
    print(cadena, "NO es un identificador válido")
'''
'''
# el del examen de comprobar un código
patron1 = r"[A-ZÑ]{3}-[0-9]{3}"
patron2 = r"[A-ZÑ]{2}-[0-9]{4}"
patron3 = r"[A-ZÑ]{2,3}-[0-9]{3,4}"
codigo = "AB-7712"
# podemos usar cualquiera de ambas condiciones del if para validar
# if re.fullmatch(patron1, codigo) or re.fullmatch(patron2, codigo):
if re.fullmatch(patron3, codigo) and len(codigo) == 7:
    posicion = codigo.find("-")
    sumando1 = int(codigo[posicion+1])
    sumando2 = int(codigo[posicion+2])
    suma = int(codigo[posicion+3:])
    if sumando1 + sumando2 == suma:
        print(codigo, "es válido")
    else:
        print(codigo, "no es válido")
else:
    print(codigo, "NO es un código válido")
'''
'''
# el de la fracción de la práctica
patronFraccion = r"[0-9]+/[1-9][0-9]*"
fraccion = ("2/")
if re.fullmatch(patronFraccion, fraccion):
    posicion = fraccion.find("/")
    numerador = int(fraccion[:posicion])
    denominador = int(fraccion[posicion+1:])
    print(fraccion, "vale", round(numerador/denominador, 3))
else:
    print(fraccion, "no es una fracción válida")
'''
# El de las matrículas de los coches
patronM1 = r"[A-Z]{1,2}-[0-9]{4}"
patronM2 = r"[A-Z]{1,2}-[0-9]{4}-[A-ZÑ]{2}"
# Añadimos en las matrículas actuales que el separador puede ser un espacio, un guión o no haber separador
patronM3 = r"[0-9]{4}[ -]?[B-DF-HJ-NPR-TV-Z]{3}"
matricula = "1234-BCD"
if re.fullmatch(patronM1, matricula):
    print(matricula, "es una matrícula antigua (1900-1971)")
elif re.fullmatch(patronM2, matricula):
    print(matricula, "es una matricula de entre 1971 y 2000")
elif re.fullmatch(patronM3, matricula):
    print(matricula, "es una matrícula actual")
else:
    print(matricula, "no es una matrícula válida en España")


