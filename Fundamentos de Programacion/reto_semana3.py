"""
Requerimiento. Escriba una función (ruteo) que reciba cómo parámetros: Un diccionario (distancias) en el cuál para una
llave (i, j) el valor correspondiente es la distancia que hay entre el lugar i y el lugar j. Y una lista (ruta_inicial) la cual
contiene el orden de visita de los distintos puntos de la ciudad según la ruta actual. Con esta información, realice el
procedimiento que se enuncia a continuación:

En cada iteración usted debe evaluar todos los posibles intercambios de dos paradas en la ruta para finalmente
actualizarla con aquel intercambio que genere la mayor reducción en la distancia total recorrida. Una vez actualizada la
ruta, debe pasar a la siguiente iteración y repetir completamente este proceso hasta que no se encuentren mejoras
adicionales (criterio de parada). Entonces, retorne un diccionario con las llaves “ruta” y “distancia” dónde, el valor
correspondiente a la primera llave sea una cadena que codifique la ruta final encontrada con las paradas separadas por
guiones y el valor correspondiente a la segunda llave sea un entero con la distancia total asociada a la ruta reportada.

Note qué Debido a la configuración vial, la distancia que se debe recorrer para ir en automóvil de un lugar i a un lugar j no
necesariamente será la misma distancia que se debe recorrer para ir del lugar j al lugar i (ida y vuelta no son equivalentes).
Independientemente de esto, la ruta siempre debe iniciar y terminar el depósito.
"""

distancias = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 0, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

def diccionario_valido(distancias):

    flag = False
    for key, value in distancias.items():        

        if value >= 0:
            if key[0] == key[1]:
                tupla_pos1 = key[0]
                tupla_pos2 = key[1]
                tupla_iguales = (tupla_pos1, tupla_pos2)
                #print(distancias[tupla_iguales])
                if distancias[tupla_iguales] == 0:
                    flag = True
                else:
                    return False
              
            # i = 0
            # while distancias[tupla_iguales][i] == 0:
            #     bandera = True
        else:
            return False
        #print(tupla_iguales)
    return flag

def calculo_distancia(ruta_inicial, distancias):

    # Iniciar contador
    i = 0
    suma = 0
    while i <= len(ruta_inicial) - 1:

        
        # Armar las tuplas
        pos1 = ruta_inicial[i]
        pos2 = ruta_inicial[i+1]
        tupla = (pos1, pos2)
        suma = suma + distancias[tupla]
        i += 1

        # Evitar la ultima iteracion de la ruta
        if (i == len(ruta_inicial) - 1):
            i = len(ruta_inicial) + 1

    return suma

def intercambio(tupla, ruta):

    nueva_ruta = ruta.copy()
    # Tomar los indices de cada posicion en las tuplas
    index_pos1 = nueva_ruta.index(tupla[0])
    index_pos2 = nueva_ruta.index(tupla[1])
    nueva_ruta[index_pos1] = tupla[1]
    nueva_ruta[index_pos2] = tupla[0]
    return nueva_ruta
        
def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    
    # Validar si los datos del diccionario DISTANCIAS son correctos
    if diccionario_valido(distancias):

        # Copiar lista inicial
        ruta_inicial_copia = ruta_inicial.copy()
        # Calculo de la distancias en la ruta inicial y en la ruta nueva
        distancia_ruta_inicial = calculo_distancia(ruta_inicial, distancias)
        bandera = False
        i = 1
        while i <= len(ruta_inicial) - 2:
            pos1 = ruta_inicial[i]
            j = i + 1
            while j <= len(ruta_inicial) - 2:
                pos2 = ruta_inicial[j]
                combinacion = (pos1, pos2)
                # Creacion de nueva lista para el intercambio de tuplas (FUNCION)
                ruta_nueva = intercambio(combinacion, ruta_inicial_copia)                
                distancia_nueva_ruta = calculo_distancia(ruta_nueva, distancias)
                if distancia_nueva_ruta < distancia_ruta_inicial:
                    ruta_optima = ruta_nueva
                    distancia_optima = distancia_nueva_ruta
                    # Actualizar la distancia de la ruta inicial
                    distancia_ruta_inicial = distancia_optima
                    bandera = True                
                j += 1
            i += 1

            if bandera and i == len(ruta_inicial) - 2:
                i = 1
                ruta_inicial_copia = ruta_optima.copy()
                bandera = False
            if not bandera and i == len(ruta_inicial) - 2:
                ruta_esperada = '-'.join(ruta_inicial_copia)
                return {'ruta': ruta_esperada, 'distancia': distancia_optima}

    
    else:
        # Revisar los datos de entrada en el Diccionario
        return "Por favor revisar los datos de entrada."


print(ruteo(distancias, ruta_inicial))

