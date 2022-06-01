''' Alejandro Otaiza Orellano - Taller consultas Covid
'''

import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

# Conocer las dimensiones del archivo
data.shape

# Conocer las columnas del arhivo
data.columns

# Cantidad de elementos del arhivo
data.size

# Para saber cuantos registros hay por columna

data.count()

# Eliminar columnas de un dataset

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)







# Normalizar la columna de Estado

data.loc[data['Estado'] == 'leve', 'Estado'] = 'Leve'
data.loc[data['Estado'] == 'LEVE', 'Estado'] = 'Leve'

# Normalizar columna sexo

data.loc[data['Sexo'] == 'm','Sexo'] = 'M'
data.loc[data['Sexo'] == 'f','Sexo'] = 'F'

# Normalizar columna Estado

data.loc[data['Estado'] == 'M','Estado'] = 'Moderado'

#Normalizar Colunmna Ubicación del caso
data.loc[data['Ubicación del caso'] == 'casa','Ubicación del caso'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA','Ubicación del caso'] = 'Casa'

#Normalizar Colunmna Recuperado 
data.loc[data['Recuperado'] == 'fallecido','Recuperado'] = 'Fallecido'


#Normalizar Columna Departamento
data.loc[data['Nombre departamento'] == 'BOGOTA','Nombre departamento'] = 'CUNDINAMARCA'
data.loc[data['Nombre departamento'] == 'BARRANQUILLA','Nombre departamento'] = 'ATLANTICO'
data.loc[data['Nombre departamento'] == 'CARTAGENA','Nombre departamento'] = 'BOLIVAR'
data.loc[data['Nombre departamento'] == 'Santander','Nombre departamento'] = 'SANTANDER'
data.loc[data['Nombre departamento'] == 'Cundinamarca','Nombre departamento'] = 'CUNDINAMARCA'
data.loc[data['Nombre departamento'] == 'Tolima','Nombre departamento'] = 'TOLIMA'
data.loc[data['Nombre departamento'] == 'Caldas','Nombre departamento'] = 'CALDAS'
data.loc[data['Nombre departamento'] == 'STA MARTA D.E.','Nombre departamento'] = 'MAGDALENA'


#Normalizar Columna Tipo de contagio
data.loc[data['Tipo de contagio'] == 'comunitaria', 'Tipo de contagio'] = 'Comunitaria'







#TALLER



''' 1. Número de casos de Contagiados en el País. '''

Casos = data['fecha reporte web'].count()
print(f'Numero de contagios {Casos}')


''' 2. Número de Municipios Afectados '''


municipios = data['Nombre municipio'].value_counts()
print('Numero de municipios afectados:\n', municipios.count())


''' 3. Liste los municipios afectados (sin repetirlos) '''

lista_nombres_municipios = list(data['Nombre municipio'].drop_duplicates())
print('Lista nombre municipios: \n', lista_nombres_municipios)


''' 4. Número de personas que se encuentran en atención en casa '''


aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
cantidad_atencion_casa = aux.shape[0]
print('Personas que se encuentran en atención en casa:\n',cantidad_atencion_casa)


''' 5. Número de personas que se encuentran recuperados '''


aux = data.loc[(data['Recuperado'] == 'Recuperado')]
cantidad_recuperados = aux.shape[0]
print('Personas recuperadas:\n',cantidad_recuperados)


''' 6. Número de personas que ha fallecido '''


aux = data.loc[(data['Recuperado'] == 'Fallecido')]
cantidad_fallecidos = aux.shape[0]
print('Personas recuperadas:\n',cantidad_fallecidos)


''' 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado) '''

tipos_casos = data['Tipo de contagio' ].value_counts().sort_values(ascending=(False))
print('Tipos de contagios de mayor a menor: \n', tipos_casos)


''' 8. Número de departamentos afectados '''


departamentos = data['Nombre departamento'].value_counts()
print('Numero de departamentos afectados:\n', departamentos.count())


''' 9. Liste los departamentos afectados(sin repetirlos) '''


lista_nombres_departamentos = list(data['Nombre departamento'].drop_duplicates())
print('Lista departamentos afectados: \n', lista_nombres_departamentos)


''' 10. Ordene de mayor a menor por tipo de atención '''


atencion = data['Ubicación del caso' ].value_counts().sort_values(ascending=(False))
print('Tipo de atencion de mayor a menor: \n', atencion)


''' 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados '''


aux = data['Nombre departamento' ].value_counts().head(10)
print('10 departamentos con mas contagios: \n', aux)


''' 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos '''


dep_fallecidos = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()
dep_fallecidos = dep_fallecidos.sort_values(ascending=(False)).head(10)
print('10 departamentos con mas fallecidos: \n', dep_fallecidos)


''' 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados '''


dep_recuperados = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()
dep_recuperados = dep_recuperados.sort_values(ascending=(False)).head(10)
print('10 departamentos con mas recuperados: \n', dep_recuperados)


''' 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados '''


aux = data['Nombre municipio' ].value_counts().sort_values(ascending=(False)).head(10)
print('10 municipios con mas contagios: \n', aux)


''' 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos '''


mun_fallecidos = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()
mun_fallecidos = mun_fallecidos.sort_values(ascending=(False)).head(10)
print('10 municipios con mas fallecidos: \n', mun_fallecidos)


''' 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados '''

mun_recuperados = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()
mun_recuperados = mun_recuperados.sort_values(ascending=(False)).head(10)
print('10 municipios con mas recuperados: \n', mun_recuperados)


''' 17. Liste agrupado por departamento y en orden de Mayor a menor las
ciudades con mas casos de contagiados '''

grup_casos = data.groupby(['Nombre departamento','Nombre municipio']).size()
grup_casos = grup_casos.sort_values(ascending=(False)).head(10)
print('10 Ciudades con departamentos con mas contagios: \n', grup_casos)

''' 18. Número de Mujeres y hombres contagiados por ciudad por
departamento '''

grup_casos = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).size()
grup_casos = grup_casos.sort_values(ascending=(False)).head(10)
print('Contagios segun hombres y mujeres por ciudad: \n', grup_casos)

''' 19. Liste el promedio de edad de contagiados por hombre y mujeres por 
ciudad por departamento '''

grup_casos = data.groupby(['Nombre departamento','Nombre municipio','Sexo'])['Edad'].agg(['mean'])
print('Promedio de edad de contagios, por hombre y mujer: \n', grup_casos)


''' 20. Liste de mayor a menor el número de contagiados por país de
procedencia '''

aux = data['Nombre del país' ].value_counts().sort_values(ascending=(False))
print('Paises con mas procedencia de contagios: \n', aux)


''' 21. Liste de mayor a menor las fechas donde se presentaron mas
contagios '''

aux = data['fecha reporte web' ].value_counts().sort_values(ascending=(False))
print('Fechas donde se presentarion mas contagios: \n', aux)


''' 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda
Colombia '''


cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
cantidad_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]

cantidad_casos = data.shape[0]

tasa_mortalidad = cantidad_muertes / cantidad_casos * 100
tasa_recuperados = cantidad_recuperados / cantidad_casos * 100

print(f'Tasa de recuperados: {tasa_recuperados}\nTasa de mortalidad: {tasa_mortalidad}')


''' 25. Liste por cada ciudad la cantidad de personas por atención '''


aux = data.groupby(['Nombre municipio','Ubicación del caso']).size()
print('Cantidad de personas por atencion: \n', aux)


''' 26. Liste el promedio de edad por sexo por cada ciudad de contagiados '''


aux = data.groupby(['Nombre municipio','Sexo'])['Edad'].agg(['mean'])
print('Promedio de edad de contagios en ciudad por hombre y mujer: \n', aux)


''' 30. Liste de mayor a menor la cantidad de fallecidos por edad en toda
Colombia. '''

aux = data[(data['Estado'] == 'Fallecido')].groupby('Edad').size()
aux = aux.sort_values(ascending=(False)).head(10)
print('Cantidad de personas por atencion: \n', aux)




















