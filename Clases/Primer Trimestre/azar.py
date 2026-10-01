import random

# En python la librería para generar números aleatorios se llama random
# hay que importarla explicitamente como está aquí arriba escrito, muy similar a como hacemos en Java
# random genera un número aleatorio entre 0 (incluido) y 1.0 (no incluido, es decir, lo máximo es 0.9999999999)
# igual que en java
print(random.random())

# randint genera un número aleatorio entre dos dados, incluidos ambos extremos
dado = random.randint(1,6)
print(dado)

# Si queremos generar un número aleatorio decimal entre dos extremos usamos la función uniform
print(random.uniform(0.5,0.75))
# o también
print(random.uniform(5,7))

# veremos mas funciones útiles relacionadas con esto mas adelante, cuando veamos otras estructuras de datos apropiadas