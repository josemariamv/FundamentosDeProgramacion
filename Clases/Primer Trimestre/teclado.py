# La función input me permite leer del teclado
nombre = input("Escribe tu nombre: ")
# Cuando python se encuentra una función input detiene la ejecución del programa
# A continuación muestra el mensaje que ponemos como argumento (entre paréntesis)
# y, por último, espera a que escribas en el teclado hasta que pulsas la tecla Intro
# Cuando lo haces, recoge todo lo que hayas escrito (salvo la propia pulsación de Intro) y lo guarda
# en la variable que has puesto a la izquierda del signo igual
print("Tú nombre es", nombre)

# Input siempre lee lo que escribas como texto
edad = input("Escribe tu edad")
# En este caso, si tu escribes un número (tu edad) el guardaría en la variable un texto con los caracteres numéricos
# Por ejemplo, "57" en lugar de 57
# Eso quiere decir que no puedes hacer operaciones aritméticas con lo que escribas

# Para convertirlo a un número entero o un número con decimales, hacemos lo siguiente:
edad = int(input("Escribe tu edad"))
sueldo = float(input("Escribe tu sueldo"))
# Recuerda que usamos el . como signo decimal
# Y que si lo que escribes no puede convertirse en un entero o en un número con decimales respectivamente
# el programa fallará y provocará una excepción
# Ya veremos mas adelante como solventar estas situaciones