# llamando a funciones
def autor():
    return "Vargas Llosa"

print(f"Hola Python, dime el autor del libro: {autor()}")

# condicionales
print(f"¿num1 es par? {True if num1 %2 == 0 else False}")

puntuacion = 85
print(f"Resultado: {'Aprobado' if puntuacion >= 50 else 'Suspenso'}")

valor = 42
print(f"Valor: {'Alto' if valor > 75 else 'Medio' if valor > 25 else 'Bajo'}")