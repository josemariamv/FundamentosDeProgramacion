import mysql.connector
from contextlib import closing

def insertarPokemon(codigo, nombre, peso, altura, tipo1, tipo2=None):
    try:
        with closing(mysql.connector.connect(user='admin', password='1234', host='localhost', database='pokemondb')) as connect:
            with closing(connect.cursor()) as cursor:
                # Para evitar que salte una excepción comprobamos antes que el pokemon no esté
                # Las fstrings son muy útiles para componer sentencias sql. Dales un repaso si no te acuerdas de ellas
                cursor.execute(f"SELECT * FROM pokemon WHERE numero_pokedex = {codigo}")
                resultado = cursor.fetchall()
                # fetchall me devuelve una lista de tuplas con el resultado. Como numero_pokedex es clave primaria
                # o hay 0 resultados o hay 1. No hay mas posibilidades
                if len(resultado) !=0:
                    # Si es distinto de 0 es que ya está
                    print("Ya hay un pokemon con código", codigo, "en la pokedex")
                else:
                    # En caso contrario, insertamos el pokemon
                    cursor.execute(f"INSERT INTO pokemon VALUES({codigo}, '{nombre}', {peso}, {altura})")
                    # buscamos el código de los tipos. Si tipo2=None solo va a encontrar el código del tipo1
                    cursor.execute(f"SELECT id_tipo FROM tipo WHERE nombre = '{tipo1}' OR nombre = '{tipo2}'")
                    # recogemos los resultados, que serán uno o dos tipos, e insertamos los registros
                    # en la tabla pokemon_tipo
                    resultado = cursor.fetchall()
                    for linea in resultado:
                        #inserto el registro en la tabla pokemon_tipo
                        cursor.execute(f"INSERT into pokemon_tipo VALUES ({codigo}, {linea[0]})")
                    # Por último, que no se te olvide hacer commit o los cambios no se guardarán!
                    connect.commit()
    except mysql.connector.Error as err:
        print(err)

# Pikachu con codigo 25 ya está
insertarPokemon(25,"Pikachu",6.0, 0.4, "Eléctrico")
# chikorita y hoothoot no estan
insertarPokemon(152,"Chikorita",6.4,0.9,"Planta")
insertarPokemon(163,"Hoothoot",21.2,0.7,"Normal", "Volador")