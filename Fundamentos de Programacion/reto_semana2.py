"""
Utilizando python, escriba una función que reciba como parámetro un diccionario en el cuál las llaves son los nombres de
las variables mencionadas anteriormente. Retorne un nuevo diccionario con las llaves “id_prestamo” y “aprobado” dónde
esta última tenga como valor una variable booleana representando la salida del árbol de decisión. Es decir, informando si
el préstamo debe ser aprobado o no.
"""

"""
Esqueleto de la funcion
    def prestamo(informacion: dict) -> dict:
        pass
"""

def prestamo(informacion: dict) -> dict:
    
    # Variables para evaluar condicionales
    i_d = informacion['ingreso_deudor']
    i_c = informacion['ingreso_codeudor']
    c_p = informacion['cantidad_prestamo']
    historial = informacion['historia_credito']
    dependientes = informacion['dependientes']
    independiente = informacion['independiente']
    casado = informacion['casado']
    t_p = informacion['tipo_propiedad']
    educacion = informacion['educacion']  

    # Dependientes = 3+
    if isinstance(dependientes, str):
        str_depend = dependientes.replace('+','')
        dependientes = int(str_depend)       


    # Evaluar Arbol de decision - para Historial = 1
    if historial == 1:
        if i_c > 0 and i_d / 9 > c_p:
            # Se cumple PRESTAMO
            aprobado = True
        else:
            if dependientes > 2 and independiente == 'Si':
                if i_c/12 > c_p:
                    # Se cumple PRESTAMO
                    aprobado = True
                else:
                    # No se cumple PRESTAMO
                    aprobado = False
            else:
                if c_p < 200:
                    # Se cumple PRESTAMO
                    aprobado = True
                else:
                    # No se cumple PRESTAMO
                    aprobado = False

    # Para Historial = 0
    else:
        if independiente == "Si":

            if not (casado == "Si" and dependientes > 1):

                if i_d/10 > c_p or i_c/10 > c_p:

                    if c_p < 180:
                        # Se cumple PRESTAMO
                        aprobado = True
                    else:
                        # No se cumple PRESTAMO
                        aprobado = False
                else:
                    # No se cumple PRESTAMO
                    aprobado = False
            else:
                # No se cumple PRESTAMO
                aprobado = False

        else:
            if (t_p != "Semiurbano" and dependientes < 2):

                if educacion == "Graduado":

                    if i_d/11 > c_p and i_c/11 > c_p:
                        # Se cumple PRESTAMO
                        aprobado = True
                    else:
                        # No se cumple PRESTAMO
                        aprobado = False
                else:
                    # No se cumple PRESTAMO
                    aprobado = False
            else:
                # No se cumple PRESTAMO
                aprobado = False

    respuesta_credito = {
        'id_prestamo': informacion['id_prestamo'],
        'aprobado': aprobado
    }

    return(respuesta_credito)
    
# Definicion de Diccionario para informacion del crédito
informacion = {
    'id_prestamo': 'RETOS2_001',
    'casado': 'No',
    'dependientes': '3+',
    'educacion': 'Graduado',
    'independiente': 'Si',
    'ingreso_deudor': 4692,
    'ingreso_codeudor': 0,
    'cantidad_prestamo': 106,
    'plazo_prestamo': 360,
    'historia_credito': 1,
    'tipo_propiedad': 'Rural'
}

print(prestamo(informacion))







    