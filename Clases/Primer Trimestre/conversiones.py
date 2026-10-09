# convertir entre tipos numéricos
precio = 45.56
precio_truncado = int(precio)
print(precio_truncado)

edad = 55
edad_con_decimales = float(edad)
print(edad_con_decimales)

#redondeo y truncado de decimales

# Convertir entre tipos numéricos y textos
texto = str(precio)
texto2 = str(precio_truncado)

# convertir entre textos y tipos numéricos
entero = int("45")
decimales = float("45.66")

# La función type me dice de que tipo es una variable
# Es importante en algunas situaciones ya que no es un lenguaje tipado
print(type(entero))
print(type(decimales))
print(type(texto))
print(type(texto2))

# Para comprobar de que tipo es una variable antes de meter la pata con una operación
# inadecuada podemos usar type
if type(precio_truncado) is int:
    print("Es un entero")

# O también, mas recomendado, la función isinstance
if isinstance(precio, float):
    print("Es un número con decimales")
