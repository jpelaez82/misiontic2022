# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Escriba una función qué reciba cómo parámetros: una cadena con el código alfanumérico del estudiante y cinco números
enteros (nota1, nota2, nota3, nota4, nota5) que representan las notas de los quices del semestre y retorne una cadena
de caracteres que le proporciona al profesor la información que desea obtener. La cadena debe tener la siguiente
estructura: "El promedio ajustado del estudiante {código} es: {promedio}" dónde, el promedio reportado debe cumplir
con las especificaciones mencionadas anteriormente (redondeado a dos decimales, en escala de 0 a 5 y calculado
eliminando la peor de las cinco notas del estudiante).
"""

def nota_quices(código: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
 ''' Nota quices
 :Parámetros:
 codigo (str): codigo único alfanumérico del estudiante
 nota1 (int): Nota del primer quiz reto semestre (0 - 100)
 nota2 (int): Nota del segundo quiz del semestre (0 - 100)
 nota3 (int): Nota del tercer quiz del semestre (0 - 100)
 nota4 (int): Nota del cuarto quiz del semestre (0 - 100)
 nota5 (int): Nota del quinto quiz del semestre (0 - 100)
 Retorno:
 String: de la forma "El promedio ajustado del estudiante {codigo} es: {promedio}" dónde, el promedio se
 calcula eliminando la peor nota y se reporta con dos decimales utilizando la escala numérica de 0 a 5
 '''

 # Paramétros de Función
 #  codigo = 'AA0010278'
 #  nota1 = 98
 #  nota2 = 69
 #  nota3 = 87
 #  nota4 = 47
 #  nota5 = 50

 # Encontrar minima nota a ser eliminada
 minimo = min(nota1, nota2, nota3, nota4, nota5)

 # Calcular promedio de notas (se usa otra variable distinta a promedio)
 prom = (nota1 + nota2 + nota3 + nota4 + nota5 - minimo) / 4

 # Promedio con nota decimal
 promedio = (prom * 5) / 100

 # Redondear promedio nota decimal
 promedio = round(promedio, 2)

 # Salida
 return "El promedio ajustado del estudiante {} es: {}".format(código, promedio)
 
 pass

# Para comprobar la funcion
print(nota_quices("AA0010276", 45, 78, 33, 81, 93))






