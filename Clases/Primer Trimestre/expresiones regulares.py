import re

# Una expresión regular no es mas que un patrón que usamos para buscar
# coincidencias en cadenas de texto para identificar si cumplen con lo que
# esperamos: un dni, un número de teléfono, una matrícula de coche, etc.
# las cadenas de texto que empiezan por r se llaman raw-strings
# y son las que tenemos que usar como patron de una expresión regular
patron = r"ola"
if re.match(patron, "ola"):
    print("Coincide")
else:
    print("No coincide")

# podemos usar indistintamente variables o literales
# Las expresiones regulares son strings encabezadas por la letra r
texto = "lola"
if re.match(r"lola", texto):
    print("Coincide")
else:
    print("No coincide")

# IMPORTANTE: match no devuelve True, cuidado. Si lo hacemos igualando a True no funciona!

print(re.match(r"ola", "ola"))
print(re.match(r"ola", "caracola"))

# el metodo search funciona de forma similar a match

if re.search(r"ola", "caracola"):
    print("Coincide")
else:
    print("No coincide")

# match solo da por bueno si la coincidencia está al comienzo de la cadena
# search da por bueno si la coincidencia está en cualquier lugar de la cadena
# si queremos que la cadena coincida exactamente con el patrón usamos fullmatch

if re.fullmatch(r"ola", "olarrr"):
    print("Coincide")
else:
    print("No coincide")

# Las expresiones regulares siguen las mismas reglas que en cualquier otro
# lenguaje. Veamos algunos ejemplos

if re.fullmatch(r"[0-9]{8}[A-Za-z]", "28999777X"):
    print("Es un DNI válido")
else:
    print("No es un DNI válido")

if re.fullmatch(r"[a-z]+", "abc"):
    print("Cualquier secuencia de letras minúsculas. Una mínimo")
else:
    print("No es válido")

if re.fullmatch(r"[1-9]|1[0-2]", "22"):
    print("Es un mes")
else:
    print("No es válido")

if re.fullmatch(r"[0-9]{4}[-|\s]?[A-Z]{3}", "6311*MXP"):
    print("Es una matrícula válida")
else:
    print("No es válido")

if re.fullmatch(r"(\w+)", "ban_derola9"):
    print("Es válida caracteres alfanuméricos. el único símbolo permitido es el _")
else:
    print("No es válido")

if re.fullmatch(r"[^579]", "7"):
    print("Cualquier cosa que no sea un 5, un 7 o un 9")
else:
    print("No es válido")

# ?! es un "negative lookahead". Quiere decir que si lo que viene a continuación coincide con lo que acompaña
# a este signo no se dará como válido. Es una forma de hacer exclusiones
if re.fullmatch(r"(?!HO)[A-Z]{2}", "XO"):
    print("Cadena de dos caracteres en mayúsculas que no sean HO")
else:
    print("No son dos caracteres en mayúsculas o es HO")


'''
OTROS PATRONES ÚTILES:

r"-?\d+"                                    # valida un entero de cualquier longitud (un dígito mínimo)
r"-?\d+(?:[.,]\d+)?"                        # valida un número con decimales (usando tanto el punto como la coma)
r"\d{5}"                                    # código postal español
r"[67]\d{8}"                                # teléfono mófil español
r"[67]\d{2}[ ]?\d{2}[ ]?\d{2}[ ]?\d{2}"     # teléfono móvil con espacios como separador
r"\d{8}-?[A-Za-z]"                          # DNI
r"\d{4}\s?[BCDFGHJKLMNPRSTVWXYZ]{3}"        # matrícula actual española
r"[\w.+-]+@[\w-]+\.[\w.]+"                  # email (no muy estricto)
r"\d{2}/\d{2}/\d{4}"                        # fecha en formato dd/mm/yyyy
r"([01]\d|2[0-3]):[0-5]\d""                 # hora en formato hh:mm
r"https?://[^\s]+"                          # URL de Internet
r"(?:\d{1,3}\.){3}\d{1,3}"                  # IPv4 (no muy estricto)
r"#\w+"                                     # hashtag
r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+"                  # sólo letras. cualquier combinación. mayúsculas, minúsculas y con tildes
r"\s{2,}"                                   # detecta espacios de mas (2 mínimo, cualquier cantidad)
r"(?=.*[A-Z])(?=.*\d).{8,}"                 # Contraseña de mas de ocho caractéres que incluya mayúsuclas y dígitos
r"#(?:[0-9a-fA-F]{3}){1,2}"                 # color en formato hexadecimal

'''