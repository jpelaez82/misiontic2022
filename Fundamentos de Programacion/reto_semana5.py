import pandas as pd
import os 

# Validar Extension CSV del archivo de datos
ruta_archivo_csv = "C:/misiontic2022/owid-covid-data.csv"
ext = ruta_archivo_csv.split(".")
myext = ext[-1]

if myext == 'csv':
    try:
        # Crear dataframe
        df = pd.read_csv('owid-covid-data.csv',                
                    usecols=[
                    "date",
                    "continent",
                    "total_cases_per_million",
                    "population",
                    "hospital_beds_per_thousand"
                    ])

        # Fecha en formato DATETIME en Pandas
        df["date"]= pd.to_datetime(df["date"]) 

        # Separacion en GRUPOS por CONTINENTE 
        africa = df[df.continent == 'Africa']
        africa.set_index('date', inplace=True)
        africa['total_cases'] = africa['total_cases_per_million'] * africa['population'] / 1000000
        africa['total_beds'] = africa['hospital_beds_per_thousand'] * africa['population'] / 1000
        print(africa)

        europe = df[df.continent == 'Europe']
        europe.set_index('date', inplace=True)
        europe['total_cases'] = europe['total_cases_per_million'] * europe['population'] / 1000000
        europe['total_beds'] = europe['hospital_beds_per_thousand'] * europe['population'] / 1000
        print(europe)

        asia = df[df.continent == 'Asia']
        asia.set_index('date', inplace=True)
        asia['total_cases'] = (asia['total_cases_per_million']/asia['population']) * 1000000
        #print(asia)

        north_america = df[df.continent == 'North America']
        north_america.set_index('date', inplace=True)
        north_america['total_cases'] = (north_america['total_cases_per_million']/north_america['population']) * 1000000
        #print(north_america)

        south_america = df[df.continent == 'South America']
        south_america.set_index('date', inplace=True)
        south_america['total_cases'] = (south_america['total_cases_per_million']/south_america['population']) * 1000000
        #print(south_america)

        # Calculo de TOTAL CASOS
        # Formula: TotalCasos_porMillon / PoblacionTotal * 1.000.000


        # dato = df.groupby('continent').total_cases_per_million.mean()

        # Formato FECHA para tipo Pandas 
        # dato = pd.to_datetime(df.date)

        # Agrupar for Fechas y por Continentes
        # print (df.groupby(['date','continent']).groups)


        # Agrupar data series por CONTINENTE
        # continentes = df.groupby('continent').total_cases_per_million
        pass
    except:
        print("Error al leer el archivo de datos.")
        pass    
    

else: 
    print("Extensión inválida.")




