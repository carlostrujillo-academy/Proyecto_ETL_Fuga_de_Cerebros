#  Proyecto ETL: Análisis de factores socioeconómicos y demográficos influyentes en la migración cualificada de Colombia.

Este proyecto integra varios módulos para realizar **ETL, análisis estadístico, scraping de salarios y geolocalización de municipios en Colombia**.  
Está orientado a estudiar los **flujos migratorios de colombianos en el exterior**, los **promedios salariales por categoría laboral** y la **distribución geográfica de ciudades**.  

---

##  Módulos Implementados

### 1) ETL y Análisis de Migración (`main.py`)
- Lectura de dataset CSV con registros de colombianos en el exterior.  
- Filtrado por años (2021–2024), edades (18–70 años) y país de nacimiento.  
- Análisis estadístico y descriptivo:
  - Evolución anual de registros.  
  - Distribución de edades con curva normal ajustada.  
  - Conteo por género, áreas de conocimiento, ciudades y países destino.  
- Visualizaciones:
  - Gráficos con **Matplotlib** y **Plotly**.  
  - Mapas interactivos con **Mapbox**.  
  - Diagrama de flujo migratorio tipo **Sankey**.  
- Exportación a CSV/Excel.  
- Inserción masiva de datos en **MySQL**.  

---

### 2) Web Scraping y Análisis Salarial (`scraper_salarios.py`)
- Web scraping en **Computrabajo** para extraer salarios por categorías laborales.  
- Extracción de **puestos, salarios promedio, rangos salariales y cantidad de registros**.  
- Limpieza de salarios (conversión a valores enteros en COP).  
- Cálculo de promedios salariales por categoría.  
- Análisis comparativo con **EE.UU y Canadá**, usando **OpenAI API**:
  - Conversión a COP con tasa de $3.900.  
  - Relación entre diferencias salariales y flujos migratorios.  
- Exportación de resultados a CSV/Excel.  
- Inserción de datos en tabla **MySQL (`categ_promedi_salarial`)**.  

---

### 3) Geolocalización de Ciudades Colombianas (`geolocalizacion.py`)
- Lectura de un Excel con nombres de **ciudades y departamentos**.  
- Obtención de coordenadas **Latitud/Longitud** usando **Geopy + Nominatim**.  
- Asignación de coordenadas ciudad por ciudad (con pausas para no saturar el servidor).  
- Exportación a un nuevo Excel con las coordenadas geográficas.  

---

##  Requisitos

- **Python 3.8+**  
- **MySQL Server** (si se desea cargar datos en base de datos). 
- **XAMPP**

### Librerías necesarias **(Crear archivo requirements.txt)**

```
pandas
numpy
matplotlib
tabulate
scipy
plotly
ipympl
mplcursors
openpyxl
mysql-connector-python
requests
beautifulsoup4
geopy
openai  
```

Instalación:

```bash
pip install -r requirements.txt
```

---

## Estructura del Proyecto

```
Proyecto_ETL_INFERENCIA_ESTADISTICA/
│
├── Database/
│   ├── Colombianos_registrados_en_el_exterior_20250917.csv
│   ├── Dataframe_Fracmentados_filtrados/
│   ├── muestra_aleatoria_1000.*
│   └── validacion_municipios.xlsx
│
├── Recopilación_Geolocalizacion/
│   └── colombia-municipios.json
│
├── main.py                # ETL + análisis migración
├── scraper_salarios.py    # Web Scraping de salarios
├── geolocalizacion.py     # Geolocalización de municipios colombianos
└── README.md
```

---

## Ejecución

### 1. **Análisis Migratorio**
```bash
python main.py
```

### 2. **Scraping y Análisis Salarial**
```bash
python scraper_salarios.py
```

### 3. **Geolocalización de Municipios**
```bash
python geolocalizacion.py
```
---

## Notebooks disponibles

- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cetrujillo/Proyecto_ETL_INFERENCIA_ESTADISTICA/blob/main/src/main.ipynb) `main.ipynb`
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cetrujillo/Proyecto_ETL_INFERENCIA_ESTADISTICA/blob/main/src/scraper_salarios.ipynb) `scraper_salarios.ipynb`
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cetrujillo/Proyecto_ETL_INFERENCIA_ESTADISTICA/blob/main/src/geolocalizacion.ipynb) `geolocalizacion.ipynb`

---

## Resultados

- **Migración** → Gráficos anuales, distribución de edades, top ciudades y países destino.  
- **Salarios** → Promedios por categoría laboral, comparación internacional con EE.UU y Canadá.  
- **Geolocalización** → Archivo Excel con coordenadas actualizadas (lat/lon) de municipios colombianos.  

---

## Contribución

1. Haz un **fork** del repositorio.  
2. Crea una rama:  
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```  
3. Envía un **Pull Request**.  

---

## Licencia

Este proyecto se distribuye bajo licencia **MIT**.  
Libre para uso académico y profesional.  
