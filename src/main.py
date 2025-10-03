# %% 
# ====Importe de librerías
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import cm, colors
import pandas as pd
import numpy as np
from tabulate import tabulate
from scipy.stats import norm
import plotly.graph_objects as go
from IPython.display import display
import mplcursors
import sys
import ipympl
import plotly.express as px
import json
import plotly.graph_objects as go

#Muestra de todas las columnas y 100 filas al imprimir DataFrame
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas al imprimir DataFrame
pd.set_option('display.max_rows', 100)      # Mostrar hasta 100 filas al imprimir DataFrame

# %% 
# =====Extracción de datos desde un archivo CSV
# Definición de la ruta del archivo CSV
data_inicial = (r"C:/Users/cetd9/OneDrive/MAESTRIA IA y CD/SEMESTRE 1/Proyecto_ETL_INFERENCIA_ESTADISTICA/Database/Colombianos_registrados_en_el_exterior_20250917.csv")
print(data_inicial)
print("Ruta del archivo CSV:", data_inicial)


# %% 
# =======Lectura del archivo CSV utilizando pandas
# Lectura del archivo CSV utilizando pandas
data_analisis = pd.read_csv(data_inicial,sep=";", encoding="ISO-8859-1", low_memory=False)
# Visualización de las primeras filas del DataFrame
print(data_analisis.head(10))


# %% 
#========Información general del DataFrame
df_titulos= data_analisis.info()
print(df_titulos)

# %%
# =====Copia del DataFrame para análisis y transformación
# Copia para trabajar sin modificar el original
data_analisis_copia = data_analisis.copy()
print(data_analisis_copia.head(20))

#%%
#=========Filtro de Año, Pais, Edades y conversión de Fechas 
#Formato de fechas en dataframe inicial es %Y-%m-%d
data_analisis_copia['Fecha de Registro'] = pd.to_datetime(data_analisis_copia['Fecha de Registro'], format='%Y-%m', errors='coerce')
data_analisis_copia['Mes_Año'] = data_analisis_copia['Fecha de Registro'].dt.strftime('%m-%Y')
data_analisis_copia['Año'] = data_analisis_copia['Fecha de Registro'].dt.year
print(data_analisis_copia.head(10))

#Filtro de datos
filtro = (
    (data_analisis_copia['Año'] >= 2021) & (data_analisis_copia['Año'] <= 2024) &
    (data_analisis_copia['Pais de Nacimiento'] == 'COLOMBIA') &
    (data_analisis_copia['Edades'] >= 18) & (data_analisis_copia['Edades'] <= 70)
)
data_analisis_copia = data_analisis_copia[filtro]

#Visualización primeras 1000 filas del dataframe copia
print(data_analisis_copia.head(1000))

# %%
# ==========Creacion de df con los datos filtrados
# Exporte del DataFrame filtrado a un archivo CSV
data_analisis_copia_to_excel = data_analisis_copia.to_excel(r"C:/Users/cetd9/OneDrive/MAESTRIA IA y CD/SEMESTRE 1/Proyecto_ETL_INFERENCIA_ESTADISTICA/Database/Dataframe_Fracmentados_filtrados/data_analisis_copia.xlsx", index=False, engine='openpyxl')
print("Filas:", data_analisis_copia.shape[0])
print("Columnas:", data_analisis_copia.shape[1])
print("Total de datos (celdas):", data_analisis_copia.size)

#%%
# =========Conteo de datos por años y por país de origen.
#Conteo de datos por años y Porcentajees (porcentajes) de cada año
conteo_año = data_analisis_copia['Año'].value_counts().sort_index()
Porcentajees = data_analisis_copia['Año'].value_counts(normalize=True).sort_index()
# Unión de un DataFrame y  Filtrar solo años 2021 a 2024
resumen = pd.DataFrame({'Conteo': conteo_año,'Porcentaje (%)': (Porcentajees * 100).round(2)})
resumen_año = resumen.loc[2021:2024].reset_index() # Seleccionar solo años 2021 a 2024
conteo_total_año= (data_analisis_copia['Año'] >= 2021) & (data_analisis_copia['Año'] <= 2024)
# print(f'Los datos del conteo anual son:{conteo_total_año}')
# print('__________________El resumen anual es:______________________')
# print(tabulate(resumen_año.reset_index(), headers="keys", tablefmt='pretty'))

#IMPLEMENTACIÓN DE TABLA ESTRUCTURADA
# Mostrar tabla con degradado
display(resumen_año.style.format({"Porcentaje (%)": "{:.2f}%"}).background_gradient(cmap='Blues', subset=['Conteo'])
        .set_properties(**{'text-align': 'center'}) # Alineación centrada de datos
        .set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]) # Alineación centrada de encabezados
)
# Estructuración de gráficos
# Gráfico de barras para la evolución anual
plt.figure(figsize=(6,4))
bars = plt.bar(resumen_año["Año"], resumen_año["Conteo"], color="orange")
# Título y etiquetas
plt.title("Evolución de Migración 2021–2024", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Número de registros", fontsize=12)
plt.xticks(resumen_año["Año"])
plt.tight_layout()

# 🔹 Agregar etiquetas de valores en cada barra
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,   # posición x centrada en la barra
        height,                            # posición y (arriba de la barra)
        f'{height:,}',                     # formato con separador de miles
        ha='center', va='bottom', fontsize=10, color='black'
    )

plt.show()

#Conteo de edades por Grupo de edad
conteo_grupo_edad = data_analisis_copia['Grupo edad'].value_counts().sort_index()
Porcentajees_edad = data_analisis_copia['Grupo edad'].value_counts(normalize=True).sort_index()
resumen_edad = pd.DataFrame({'Conteo': conteo_grupo_edad,'Porcentaje (%)': (Porcentajees_edad * 100).round(2)})
resumen_edad = resumen_edad.reset_index()
# print('__________________El conteo por grupo de edad es:______________________')
# print(tabulate(resumen_edad.reset_index(), headers="keys", tablefmt='pretty')) 
# Mostrar resultados // Datos de resumen por AÑO

# Mostrar resultados // Datos de resumen por EDAD
display(resumen_edad.style.format({"Porcentaje (%)":"{:.2f}%"}).background_gradient(cmap='Blues', subset=['Conteo'])\
        .set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))
# Estructuración de gráficos
# Gráfico de barras para la evolución anual
plt.figure(figsize=(6,4))
bars = plt.bar(resumen_edad["Grupo edad"], resumen_edad["Conteo"], color="orange")
# Título y etiquetas
plt.title("Conteo por Grupo de Edad:", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Número de registros", fontsize=12)
plt.xticks(resumen_edad["Grupo edad"])
plt.tight_layout()

# 🔹 Agregar etiquetas de valores en cada barra
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,   # posición x centrada en la barra
        height,                            # posición y (arriba de la barra)
        f'{height:,}',                     # formato con separador de miles
        ha='center', va='bottom', fontsize=10, color='black'
    )

plt.show()

# %% 
#===========Ploteo de gráficos Edades y distribución normal
# Histograma de edades con curva normal ajustada

# 1) Campana de Gauss (Distribución normal) de EDADES
plot_edad = data_analisis_copia['Edades'].dropna()
# Calcular parámetros de la normal
mu,sigma = plot_edad.mean(), plot_edad.std()
# Crear la curva normal y Rango de valores para la curva
counts, bins = np.histogram(plot_edad, bins=100)
bin_width = bins[1] - bins[0]
x = np.linspace(plot_edad.min(), plot_edad.max(), 100)
y = norm.pdf(x, mu, sigma)* len(plot_edad)*bin_width # Revisar como se comporta la curva normal


# 3. Crear histograma interactivo con curva normal
fig = go.Figure()
# Histograma
fig.add_trace(go.Histogram(x=plot_edad,nbinsx=100,histnorm=None,name="Frecuencia",marker=dict(color="lightblue",line=dict(color="black", width=1))))
# Curva normal
fig.add_trace(go.Scatter(x=x, y=y,mode="lines",name="Campana de Gauss",line=dict(color="red", width=2)))
# Personalizar layout
fig.update_layout(title="Distribución de edades con curva normal ajustada (Interactivo)",xaxis_title="Edad",yaxis_title="Frecuencia",bargap=0.1,width=800,height=500)
# Mostrar en Jupyter
fig.show()

# Imprimir media y desviación estándar
print(f"Media de las edades: {mu:.2f}")
print(f"Desviación estándar: {sigma:.2f}")

#%% NO USAR
# _________________________ ESTE FRAGMENTO DE CODIGO SE UTILIZO PARA SACAR EL Listado de ciudades unicas UTILIZADO PARA HACER ETL__________________________
# ciudades_paises = data_analisis_copia[['Pais de Nacimiento','Departamento/Estado.1','Ciudad_Origen']].drop_duplicates()
# print(ciudades_paises)
# # Exporte de la lista de ciudades y países a un archivo CSV
# ciudades_paises.to_csv(r"C:/Users/cetd9/OneDrive/MAESTRIA IA y CD/SEMESTRE 1/Proyecto_ETL_INFERENCIA_ESTADISTICA/Database/ciudades_paises.csv", index=False, encoding='utf-8-sig')

#%%
#========== Agrupación y conteo por país de nacimiento, departamento/estado y ciudad de origen
# Verificación de Países, departamentos y ciudades únicas
agrupacion = data_analisis_copia.groupby(['Pais de Nacimiento', 'Departamento/Estado.1', 'Ciudad_Origen']).size().reset_index(name='Conteo_Región')
print(tabulate(agrupacion.reset_index(), headers="keys", tablefmt='pretty'))

# %%
#==========Top 10 Ciudades con mayor cantidad de migrantes.
tablaresumen =pd.DataFrame(agrupacion)
top_10_ciudades = tablaresumen.nlargest(10,'Conteo_Región')
# Mostrar tabla con degradado de colores
display(top_10_ciudades.style.background_gradient(cmap='Blues', subset=['Conteo_Región'])\
        .set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))

#===========Ploteo de gráfico de barras para las 10 ciudades con más registros
#Detectar si estamos en un entorno interactivo (notebook) o directamente desde un script .py
def in_notebook():
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config:  # no hay kernel de Jupyter
            return False
    except Exception:
        return False
    return True

if in_notebook():
    # Para notebooks (Jupyter/VS Code .ipynb)
    # se serciora de que el backend es 'widget'
    get_ipython().run_line_magic("matplotlib", "widget")
else:
    # Para scripts .py normales
    matplotlib.use("TkAgg")   # o "Qt5Agg" si usas Qt

#____________ Ploteo de gráfico de barras para las 10 ciudades con más registros________________________

#Gráfico de barras horizontal con degradado
fig, ax = plt.subplots(figsize=(8,4)) # Tamaño de la figura

# Normalizar valores de 'Conteo_Región' entre 0 y 1 // Conversión a escala de los valores maximos y minimos del conteo de registros
n= colors.Normalize(top_10_ciudades['Conteo_Región'].min(), top_10_ciudades['Conteo_Región'].max())

# Color variable para las barras
colores = cm.Blues(n(top_10_ciudades['Conteo_Región']))

# Graficar en el eje ax
bars = ax.barh(top_10_ciudades['Ciudad_Origen'],top_10_ciudades['Conteo_Región'],color=colores)

# Crear gráfico de barras horizontal
ax.set_title('Top 10 Ciudades con más Registros', fontsize=10)
ax.set_xlabel('Conteo de Registros', fontsize=8)
ax.set_ylabel('Ciudad de Origen', fontsize=8)
ax.invert_yaxis()  # Ciudad con más registros arriba

# Colorbar asociada al gráfico
sm = plt.cm.ScalarMappable(cmap=cm.Blues, norm=n)
sm.set_array([])
fig.colorbar(sm, ax=ax, label='Conteo de Registros')

# Activar tooltips
cursor = mplcursors.cursor(bars, hover=True)
@cursor.connect("add")
def on_add(sel):
    ciudad = top_10_ciudades['Ciudad_Origen'].iloc[sel.index]
    conteo = top_10_ciudades['Conteo_Región'].iloc[sel.index]
    sel.annotation.set_text(f"{ciudad}\nRegistros: {conteo}")
    sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9)


plt.tight_layout()   # Ajusta todo automáticamente
plt.show()

#%%
#==========PROFESONALES REGISTRADOS EN CIUDADES

# Agrupación y conteo por ciudad de origen y área de conocimiento
tabla_areaconocimiento = data_analisis_copia.groupby(["Ciudad_Origen","Area Conocimiento"]).agg({'Cantidad de personas':'sum'}).reset_index()
top_20_areavsciudad =(tabla_areaconocimiento.sort_values('Cantidad de personas',ascending=False).head(20))

#Mostrar tabla con degradado de colores
display(top_20_areavsciudad.style.background_gradient(cmap='Blues', subset=['Cantidad de personas'])\
        .set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))

# Ploteo de gráfico de barras para las 10 Primeras ciudades con más profesionales registrados
top_cities = (tabla_areaconocimiento.groupby('Ciudad_Origen')['Cantidad de personas'].sum().nlargest(10).index)

df_top_cities = tabla_areaconocimiento[tabla_areaconocimiento['Ciudad_Origen'].isin(top_cities)]

# 3) Pivot: ciudades vs áreas
pivot = (df_top_cities.pivot_table(index="Ciudad_Origen",columns="Area Conocimiento",values="Cantidad de personas",aggfunc="sum",fill_value=0).loc[top_cities])

# 4) Gráfico de barras agrupadas
ax = pivot.plot(kind="bar", figsize=(12,6), width=0.8)

plt.title("Top 10 Ciudades con más Profesionales por Área de Conocimiento", fontsize=14)
plt.xlabel("Ciudad de Origen", fontsize=12)
plt.ylabel("Cantidad de Personas", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.legend(title="Área de Conocimiento", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# 5) Cursor para tooltips e interacción con el gráfico
cursor = mplcursors.cursor(ax.containers, hover=True)

@cursor.connect("add")
def on_add(sel):
    # índice de la barra
    ciudad_idx = sel.index  
    # nombre de la ciudad
    ciudad = pivot.index[ciudad_idx]
    # columna (área de conocimiento) de esa barra
    barra = sel.artist
    area = barra.get_label()
    # valor de la barra
    valor = barra.datavalues[ciudad_idx]
    # texto del tooltip
    sel.annotation.set_text(f"{ciudad}\n{area}: {valor:,}")
    sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9)

plt.show()


#%%
#==========Top 10 áreas de conocimiento con más registros

# DataFrame con las 10 áreas de conocimiento con más registros
#display(data_analisis_copia['Area Conocimiento'].value_counts().head(10).reset_index().rename(columns={'index':'Área de Conocimiento','Area Conocimiento':'Cantidad de personas'})\
#       .style.background_gradient(cmap='Blues', subset=['Cantidad de personas'])\

# Agrupación y conteo por área de conocimiento
top_areas = (data_analisis_copia.groupby("Area Conocimiento")["Cantidad de personas"].sum().nlargest(10).reset_index())

plt.figure(figsize=(8,5))
bars = plt.barh(top_areas["Area Conocimiento"], top_areas["Cantidad de personas"], color="teal")
plt.gca().invert_yaxis()

plt.title("Top 10 Áreas de Conocimiento", fontsize=14)
plt.xlabel("Número de registros", fontsize=12)
plt.ylabel("Área de Conocimiento", fontsize=12)
plt.tight_layout()

for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
             f'{bar.get_width():,}', va='center', fontsize=9)

plt.show()


#%%
#======AGRUPACIÓN POR AREA DE CONOCIMIENTO Y GENERO

# Agrupación y conteo por área de conocimiento
area_conocimiento = data_analisis_copia.groupby(['Area Conocimiento','Genero'])['Cantidad de personas'].sum().reset_index().sort_values('Cantidad de personas', ascending=False)
# Mostrar tabla bonita
top_20_areasconocimiento = area_conocimiento["Cantidad de personas"].sum()
area_conocimiento["Porcentaje (%)"] = (area_conocimiento["Cantidad de personas"] / top_20_areasconocimiento * 100).round(3) #Round a 2 decimales

#top 20 áreas de conocimiento
top_20_areasconocimiento = area_conocimiento.head(20)

#Mostrar tabla con degradado de colores
display(top_20_areasconocimiento.style.format({"Porcentaje (%)": "{:.2f}%"}).background_gradient(cmap='Blues', subset=['Cantidad de personas'])\
        .set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))

#==========Ploteo de gráfico de barras para las 20 áreas de conocimiento con más registros
# 1) Agrupar por área de conocimiento y género
area_genero = (
    data_analisis_copia
    .groupby(["Area Conocimiento","Genero"])["Cantidad de personas"]
    .sum()
    .reset_index()
)

# 2) Pivotear: cada área tendrá columnas para MASCULINO y FEMENINO
pivot = area_genero.pivot_table(
    index="Area Conocimiento", 
    columns="Genero", 
    values="Cantidad de personas", 
    fill_value=0
)

# 3) Ordenar por total de personas y tomar Top 10
pivot["Total"] = pivot.sum(axis=1)
pivot = pivot.sort_values("Total", ascending=False).head(10)
pivot = pivot.drop(columns="Total")

# 4) Gráfico de barras agrupadas
ax = pivot.plot(kind="bar", figsize=(10,6), width=0.8)

plt.title("Top 10 Áreas de Conocimiento por Género", fontsize=14)
plt.xlabel("Área de Conocimiento", fontsize=12)
plt.ylabel("Cantidad de Personas", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.legend(title="Género")
plt.tight_layout()

# 5) Tooltips dinámicos con valor + %
cursor = mplcursors.cursor(ax.containers, hover=True)

@cursor.connect("add")
def on_add(sel):
    # Índice de la fila (área de conocimiento)
    idx = sel.index
    # Género = nombre de la serie (columna en el pivot)
    genero = sel.artist.get_label()
    # Área de conocimiento
    area = pivot.index[idx]
    # Valor (conteo de personas)
    valor = sel.artist.datavalues[idx]

    # Total de personas en esa área (ambos géneros)
    total_area = pivot.loc[area].sum()
    porcentaje = (valor / total_area) * 100 if total_area > 0 else 0

    # Texto del tooltip
    sel.annotation.set_text(f"{area}\n{genero}: {valor:,} ({porcentaje:.1f}%)")
    sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9)

plt.tight_layout()   # Ajusta todo automáticamente
plt.show()

# %%
#========= Paises con más migrantes recibidos
# Agrupación y conteo por país de nacimiento
# Top 10 países de destino

top_paises = (data_analisis_copia.groupby("Pais")["Cantidad de personas"].sum().nlargest(10).reset_index())
#Tabla tipo df
display(top_paises.style.background_gradient(cmap='Blues', subset=['Cantidad de personas'])
        .set_properties(**{'text-align':'center'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]))

plt.figure(figsize=(8,5))
bars = plt.bar(top_paises["Pais"], top_paises["Cantidad de personas"], color="green")

plt.title("Top 10 Países receptores de Colombianos", fontsize=14)
plt.xlabel("País de destino", fontsize=12)
plt.ylabel("Número de registros", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():,}', ha='center', va='bottom', fontsize=9)

plt.show()

#Ploteo Grafico (Mapa conceptual de la migración y la recepción)

# ========= Agrupar datos del DataFrame =========
# Ajusta los nombres de columnas según tu DF
df_sankey = (
    data_analisis_copia.groupby(["Pais de Nacimiento", "Pais"])
    ["Cantidad de personas"]
    .sum()
    .reset_index()
)

# ========= Crear lista de nodos =========
# Nodos únicos: orígenes + destinos
nodos = list(pd.concat([df_sankey["Pais de Nacimiento"], df_sankey["Pais"]]).unique())

# Diccionario para mapear nodo → índice
mapa_indices = {pais: i for i, pais in enumerate(nodos)}

# ========= Crear enlaces (links) =========
sources = df_sankey["Pais de Nacimiento"].map(mapa_indices).tolist()
targets = df_sankey["Pais"].map(mapa_indices).tolist()
values = df_sankey["Cantidad de personas"].tolist()

# ========= Construir Sankey =========
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15, thickness=20, line=dict(color="black", width=0.5),
        label=nodos
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
)])

fig.update_layout(title="Flujos Migratorios (Origen → Destino)", title_x=0.5)
fig.show()


#%%

#Cargue de .geojson de Departamentos de Colombia.
ruta_geojson = r"C:/Users/cetd9/OneDrive/MAESTRIA IA y CD/SEMESTRE 1/Proyecto_ETL_INFERENCIA_ESTADISTICA/Recopilación_Geolocalizacion/colombia-municipios.json"

with open(ruta_geojson, "r", encoding="utf-8") as f:
    colombia_geojson = json.load(f)

# ORGANIZAR GEOREFERENCIACIONES
df = data_analisis_copia
df["Coordenada X"] = pd.to_numeric(df["Coordenada X"].astype(str).str.replace(",", "."), errors="coerce")
df["Coordenada Y"] = pd.to_numeric(df["Coordenada Y"].astype(str).str.replace(",", "."), errors="coerce")
print(df[["Coordenada X", "Coordenada Y"]].dtypes)

# ================== AGRUPAR POR CIUDAD (una burbuja por ciudad)
df_grouped = df.groupby("Ciudad_Origen").agg({
    "Cantidad de personas": "sum",
    "Coordenada X": "mean",   # o "first" si quieres la primera coordenada
    "Coordenada Y": "mean"
}).reset_index()

#================heatmap para graficar mapa de calor 
# fig1 = px.density_map(df,lat="Coordenada X",lon="Coordenada Y",z="Cantidad de personas",
#                      radius=20,center=dict(lat=4.6248, lon=-74.0937),zoom=5,map_style="open-street-map"
#                      )
# fig1.update_layout(
#     title="Mapa de Calor de Migración por Coordenadas",
#     title_x=0.5
# )

# fig1.show()

# ================== MAPA DE BURBUJAS
fig = px.scatter_mapbox(
    df_grouped,
    lat="Coordenada X",
    lon="Coordenada Y",
    size="Cantidad de personas",
    color="Cantidad de personas",
    hover_name="Ciudad_Origen",
    zoom=5,
    center=dict(lat=4.6248, lon=-74.0937),
    mapbox_style="open-street-map",
    size_max=25   # Regular el tamaño máximo de las burbujas
)

fig.update_layout(title="Mapa de Migración por Ciudad", title_x=0.5)
fig.show()


# %%
#===========Sacar muestra aleatoria de 1000 datos el ramdom_state es la semilla utilizada para la toma de datos.
muestra_aleatoria = data_analisis_copia.sample(n=1000, random_state=42)
print(muestra_aleatoria)


# %% 
#===========Exporte de la muestra aleatoria a un archivo CSV
muestra_aleatoria.to_csv(r"C:/Users/cetd9/OneDrive/MAESTRIA IA y CD/SEMESTRE 1/Proyecto_ETL_INFERENCIA_ESTADISTICA/Database/muestra_aleatoria_1000.csv", index=False, encoding='utf-8-sig')
muestra_aleatoria.to_excel(r"C:/Users/cetd9/OneDrive/MAESTRIA IA y CD/SEMESTRE 1/Proyecto_ETL_INFERENCIA_ESTADISTICA/Database/muestra_aleatoria_1000.xlsx", index=False, engine='openpyxl')

#%% 
# Conversión de fecha de registro a formato objeto datetime
df['Fecha de Registro'] = df['Fecha de Registro'].astype(str)

print(df.head(10))
print(df.dtypes)
# %%
# #===========Carga de datos a base de datos MySQL
# # Aquí se debe ajustar la conexión y los campos según la base de datos y tabla destino
# import mysql.connector
# from mysql.connector import Error

# #df = pd.DataFrame({'números': [1, 2, 3], 'letras': ['a', 'b', 'c']})

# # crear una lista anidada
# data = [tuple(x) for x in df.values.tolist()]
# print(data)

# try:
#     connection = mysql.connector.connect(host='localhost', # local host base de datos local.
#                                          port=3306,        # Puerto por defecto de MySQL
#                                          database='migracion',   # Nombre de la base de datos
#                                          user='root',       # Usuario de la base de datos
#                                          password='',
#                                          auth_plugin='mysql_native_password')   # Contraseña de la base de datos // N.A

#     if connection.is_connected():
#         cursor = connection.cursor()
#         cursor.executemany("INSERT INTO data_migracion (pais,codigo_iso,estado_destino,ciudad_migrada,oficina_registro,grupo_edad,edades,area_conocimiento,sub_area_conocimiento,nivel_academico,estado_civil,genero,etnia,estatura,pais_nacimiento,departamento_naci,ciudad_origen,x_inicial,y_inicial,fecha_registro,cant_personas,concat,pais_filtrado,coor_x,coor_y,mes_año,año) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", data)  # Insertar Datos en la tabla
#         if (len(data) == cursor.rowcount):
#             connection.commit()
#             print("Data inserted")
#         else:
#             connection.rollback()
#             print("Data not inserted")
# except Error as ex:
#   print("Error while connecting to MySQL", ex)
# finally:
#   if connection.is_connected():
#     connection.close()
#     print ("Connection Closed")

# %%
import mysql.connector
from mysql.connector import Error

#data = [tuple(x) for x in df.values.tolist()]
data = [tuple(None if pd.isna(xi) else xi for xi in x) for x in df.values.tolist()]


try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='migracion',
        user='root',
        password='',
        auth_plugin='mysql_native_password'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        batch_size = 1000
        for i in range(0, len(data), batch_size):
            cursor.executemany(
                """INSERT INTO data_migracion 
                (pais,codigo_iso,estado_destino,ciudad_migrada,oficina_registro,
                 grupo_edad,edades,area_conocimiento,sub_area_conocimiento,
                 nivel_academico,estado_civil,genero,etnia,estatura,
                 pais_nacimiento,departamento_naci,ciudad_origen,
                 x_incial,y_inicial,fecha_registro,cant_personas,concat,
                 pais_filtrado,coor_x,coor_y,mes_año,año)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s)""", 
                data[i:i+batch_size]
            )
            connection.commit()

        print(f"{cursor.rowcount} registros insertados")

except Error as ex:
    print("Error while connecting to MySQL", ex)

finally:
    if connection.is_connected():
        connection.close()
        print("Connection Closed")
