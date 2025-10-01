📊 Análisis y Dashboard de Fuga de Cerebros (Colombianos en el Exterior)
Este proyecto implementa un proceso ETL + análisis estadístico + dashboard interactivo en Dash/Plotly sobre datos de colombianos registrados en el exterior (2021–2024).

El objetivo principal es visualizar la migración de profesionales y analizar el fenómeno conocido como fuga de cerebros.
🔧 1. Importación de librerías
Se cargan todas las librerías necesarias para el análisis, visualización y creación del dashboard.
python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import mplcursors
import json
from dash import Dash, dcc, html, Input, Output

data_inicial = (r”D:/…/Colombianos_registrados_en_el_exterior_20250917.csv”)
data_analisis = pd.read_csv(data_inicial, sep=”;”, encoding=”ISO-8859-1”, low_memory=False)

Conversión de fechas
data_analisis[‘Fecha de Registro’] = pd.to_datetime(data_analisis[‘Fecha de Registro’], format=’%Y-%m’, errors=’coerce’)
data_analisis[‘Año’] = data_analisis[‘Fecha de Registro’].dt.year

3. Filtrado de información
Se seleccionan solo registros de Colombia, en el rango de 18–70 años y entre 2021–2024.
filtro = (
(data_analisis[‘Año’] >= 2021) & (data_analisis[‘Año’] <= 2024) &
(data_analisis[‘Pais de Nacimiento’] == ‘COLOMBIA’) &
(data_analisis[‘Edades’] >= 18) & (data_analisis[‘Edades’] <= 70)
)
data_analisis_copia = data_analisis[filtro]

4. Estadísticas descriptivas
Evolución anual de migración
conteo_año = data_analisis_copia[‘Año’].value_counts().sort_index()

Distribución por grupos de edad
conteo_grupo_edad = data_analisis_copia[‘Grupo edad’].value_counts().sort_index()

Distribución normal de edades
plot_edad = data_analisis_copia[‘Edades’].dropna()
mu, sigma = plot_edad.mean(), plot_edad.std()

5. Ciudades y regiones
Se analiza el Top 10 de ciudades con más migrantes.
agrupacion = data_analisis_copia.groupby([‘Pais de Nacimiento’, ‘Departamento/Estado.1’, ‘Ciudad_Origen’]).size().reset_index(name=’Conteo_Región’)
top_10_ciudades = agrupacion.nlargest(10, ‘Conteo_Región’)

6. Profesionales por área de conocimiento
Se visualizan los profesionales según área de estudio.
top_areas = (data_analisis_copia.groupby(“Area Conocimiento”)[“Cantidad de personas”].sum().nlargest(10).reset_index())

7. Flujos migratorios internacionales
Se genera un diagrama Sankey con países de origen y destino.
df_sankey = (
data_analisis_copia.groupby([“Pais de Nacimiento”, “Pais”])
[“Cantidad de personas”]
.sum()
.reset_index()
)

8. Mapas interactivos
Se usa plotly.express para graficar migración por ciudades en un mapa con burbujas.
fig = px.scatter_mapbox(
df_grouped,
lat=”Coordenada X”,
lon=”Coordenada Y”,
size=”Cantidad de personas”,
color=”Cantidad de personas”,
hover_name=”Ciudad_Origen”,
mapbox_style=”open-street-map”
)
fig.show()

9. Dashboard Interactivo (Dash)
El dashboard permite filtrar por área de conocimiento y visualizar la evolución anual y el top 10 de países receptores.
app = Dash(name)

app.layout = html.Div([
html.H1(“Dashboard de Migración Colombiana (2021–2024)”),
dcc.Dropdown(id=’area-dropdown’, options=[…]),
dcc.Graph(id=’grafico-anual’),
dcc.Graph(id=’grafico-paises’)
])
python dashboard_app.py

Accede en tu navegador a: http://127.0.0.1:8050/
📦 proyecto-fuga-cerebros
┣ 📜 README.md
┣ 📜 requirements.txt
┣ 📜 etl_proceso.py
┣ 📜 dashboard_app.py
┣ 📂 Database
┃ ┗ 📜 Colombianos_registrados_en_el_exterior_20250917.csv
┗ 📂 docs
┗ 📊 imágenes de ejemplo

