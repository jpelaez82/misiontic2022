import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def caso_who(ruta_archivo_csv: str)-> dict:

    # Validar Extension CSV del archivo de datos
    # ext = ruta_archivo_csv.split(".")
    # myext = ext[-1]

    if ruta_archivo_csv.endswith('.csv'):
        try:
            # Crear dataframe y seleccionar columnas a trabajar
            df = pd.read_csv(ruta_archivo_csv,                
                        usecols=[
                        "date",
                        "continent",
                        "total_cases_per_million",
                        "population",
                        "hospital_beds_per_thousand"
                        ])
            
            # Fecha en formato DATETIME para Pandas
            df["date"] = pd.to_datetime(df["date"]) 
            
            #  Calculo del promedio de la razón entre el número total de casos de COVID-19 y el número total de camas de hospital disponibles
            df['total_cases'] = df['total_cases_per_million'] * df['population'] / 1000000
            df['total_beds'] = df['hospital_beds_per_thousand'] * df['population'] / 1000
            df['rate'] = df['total_cases'] / df['total_beds']
            
            # Agrupar el dataframe por FECHA y CONTINENTE
            group = df.groupby(['date', 'continent'])
            # Asignar dataframe df_respuesta
            df_respuesta = group['rate'].agg(np.mean).unstack()
            
            # Grafico del Dataframe 
            df_respuesta.plot()
            plt.show()

            return df_respuesta.to_dict()
        
        except:
            return "Error al leer el archivo de datos."
        

    else: 
        return "Extensión inválida."




