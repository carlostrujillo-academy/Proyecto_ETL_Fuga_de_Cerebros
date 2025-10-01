📊 Análisis de Fuga de Cerebros en Colombia (2021–2024)
Este proyecto realiza un proceso ETL (Extracción, Transformación y Carga) y un análisis estadístico–visual sobre la migración de profesionales colombianos al exterior (fuga de cerebros).
El código está implementado en Python (Jupyter Notebook / VS Code) e incluye un Dashboard interactivo con Dash y Plotly.

📂 Estructura del proyecto
Proyecto_Fuga_Cerebros
data/ # Archivos CSV y XLSX con datos iniciales y filtrados
notebooks/ # Scripts y cuadernos Jupyter para el ETL
dashboard/ # App interactiva con Dash
outputs/ # Resultados exportados (CSV, Excel, Gráficos)
colombia-municipios.json # Archivo GeoJSON para visualización geográfica
README.md # Este archivo

🛠️ Tecnologías utilizadas
Lenguaje: Python 3.8+
Librerías de análisis: pandas, numpy, scipy, tabulate
Visualización: matplotlib, plotly, mplcursors, plotly.express
Dashboards: dash (Dash + Plotly Express)
Georreferenciación: plotly.express.scatter_mapbox con .geojson
Exportación: openpyxl (para Excel)
pandas
numpy
scipy
matplotlib
tabulate
plotly
dash
openpyxl
mplcursors
ipympl
pip install -r requirements.txt
🗄️ Ruta del archivo de datos
El script usa una variable data_inicial con la ruta del CSV. Actualiza la ruta si tu archivo está en otra ubicación:
data_inicial = r”D:/Diego Angrino Chiran/…/Colombianos_registrados_en_el_exterior_20250917.csv”
print(“Ruta del archivo CSV:”, data_inicial)

Bloque 6 — Proceso ETL y pasos principales
```markdown

🔎 Proceso ETL y Análisis
Extracción: Lectura del CSV (separador ;, codificación ISO-8859-1).
Transformación:
Conversión de fechas y creación de Mes_Año, Año.
Filtrado por años (2021–2024), país (COLOMBIA), edades (18–70).
Normalización de coordenadas y limpieza de nulos.
Carga:
Exportación a .csv y .xlsx.
Generación de muestra aleatoria (1000 registros) para validación.
📊 Visualizaciones incluidas
Evolución anual (2021–2024).
Distribución de edades con ajuste a curva normal (Campana de Gauss).
Top 10 países receptores.
Top 10 ciudades de origen.
Mapas (burbuja / heatmap) y Sankey diagram para flujos migratorios.
Gráficos por área de conocimiento y por género.
▶️ Cómo ejecutar
Ejecutar el notebook ETL (VS Code / Jupyter):
```bash
jupyter notebook notebooks/etl_fuga_cerebros.ipynb
python dashboard_app.py
Bloque 9 — Exportes y outputs
markdown

💾 Exportes / Outputs
outputs/ contiene los archivos resultantes: Excel/CSV generados por el ETL.
Ejemplos de exportación en el código:
data_analisis_copia.to_excel("outputs/data_analisis_copia.xlsx", index=False)
muestra_aleatoria.to_csv("outputs/muestra_aleatoria_1000.csv", index=False)
📜 Licencia
Este proyecto está bajo la licencia MIT. Si lo usas o modificas, agradezco que menciones la autoría.

👨‍💻 Autor
Diego Angrino Chiran
Maestría en Inteligencia Artificial y Ciencia de Datos
GitHub | LinkedIn
