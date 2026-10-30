# print tiene dos parámetros por defecto. end y sep
# cuando no los usamos, el valor por defecto que toman es end="\n" y sep=" "
# al final de la instrucción print siempre se muestra lo que haya en el parámetro end
# y como separador entre los diferentes parámetros del print se pone lo que haya en el parámetro sep
# podemos cambiar los valores por lo que nosotros necesitemos:
nombre = "José María"
edad = 57
sueldo= 2400.356

# la siguiente instrucción usa tres asteriscos como separador y al final pone tres puntos y dos saltos de línea en lugar de uno
print("Mi nombre es", nombre, "tengo", edad, "y mi sueldo es de", sueldo, "€ al mes", sep="***", end="...\n\n")

# Tenemos otra forma de usar print y es esta, usando el operador %
print("Mi nombre es %s, tengo %d años y cobro %f euros al mes"  %(nombre, edad, sueldo))
# Esta forma nos permite poner modificadores de formato. Por ejemplo, redondear los decimales a dos cifras:
print("Mi nombre es %s, tengo %d años y cobro %.2f euros al mes" %(nombre, edad, sueldo))

# Y también me permite crear cadenas:
texto = "Mi nombre es %s, tengo %d años y cobro %.2f euros al mes" %(nombre, edad, sueldo)
print(texto)

# Cuando necesito mostrar un % en este tipo de cadenas como es un símbolo especial lo tengo que duplicar:
porcentaje = 87.5
print("El total escrutado ha sido del %.2f%% del censo electoral" %(porcentaje))

# Pero el metodo mas flexible para trabajar con formato son las f-strings
lenguaje = "Python"
escuela = "IES GOYA"
print(f"Estoy aprendiendo {lenguaje} en {escuela}.")

poblacion = 1234567890
# Igualmente, las fstring se pueden usar también para crear cadenas y no solo para mostrarlas
cadena = f"La población del país es de: {poblacion} habitantes"
print(cadena)

# Puedo usar cálculos y formatear decimales
num1 = 83.3
num2 = 9.54
print(f"El producto de {num1} y {num2} es {num1 * num2}")
print(f"El producto de {num1} y {num2} es {num1 * num2 :.3f}")

# mostrar porcentajes
num3 = 0.83945
print(f"Porcentaje con 2 decimales: {num3:.2%}")

# introducir el separador de miles y millones en las cifras grandes (usando la , que es el separador anglosajón)
print(f"La población del país es de: {poblacion:,} habitantes")

# justificar números a la derecha
num4 = 45
num5 = 123
print(f"Números: {num4:4d} - {num5:4d}")

# completando con ceros a la izquierda si así lo queremos:
print(f"Números: {num4:04d} - {num5:04d}")

# o ajustando también con decimales
print(f"Números: {num1:6.2f} - {num2:6.2f}")

# Alinear textos a derecha, izquierda o centrados
texto = "Python"
print(f"A la izquierda:   ***{texto:<20}***")
print(f"A la derecha:  ***{texto:>20}***")
print(f"Centrado: ***{texto:^20}***")

# usarlo como herramienta de debug
for i in range(5):
    n = i * 0.435
    k = i / 3.456
    print(f"{i=}, {n=}, {k=}")

# Los f-string pueden tener varias líneas. Para ello usamos las triples comillas dobles
nombre = "Alicia"
cargo = "Profesora"
experiencia = 5
ficha = f"""
Ficha de usuario/a:
-------------------
Nombre: {nombre}
Puesto: {cargo}
Experiencia: {experiencia} años
"""
print(ficha)

# Como las llaves son un caracter especial, cuando necesitamos mostrarlas en una f-string hay que duplicarlas
nombre = "Python"
print(f"{{ Estoy estudiando: {nombre} }}")







