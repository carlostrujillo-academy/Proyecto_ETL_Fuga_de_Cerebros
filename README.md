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
Proyecto_ETL_Fuga_de_Cerebros/
│
├── Notebook/                     # Notebooks convertidos (.ipynb)
│   ├── main.ipynb
│   ├── scraper_salarios.ipynb
│   └── geolocalizacion.ipynb
│
├── data/                         # Datos de entrada
│   ├── import/                   # Datos originales o brutos (raw)
│   │   ├── migracion.zip
│   │   └── validacion_municipios.xlsx
│   ├── export/                # Datos procesados/listos para análisis
│   │   └── promedios_salariales_categ_colombia.csv
│   └── README.md                 # explica cada dataset
│
├── src/                          # Scripts de código Python
│   ├── main.py                   # Script principal ETL
│   ├── scraper_salarios.py       # Scraping y limpieza de salarios
│   └── geolocalizacion.py        # Geolocalización de ciudades
│
├── requirements.txt              # librerías necesarias para correr el proyecto
├── README.md                     # guía principal del proyecto
└── LICENSE (opcional)            # licencia del repositorio

```

---

## Ejecución (SE RECOMIENDA Ejecutar como archivo JUPYTER e instalar todas las librerias requeridas para el proceso) 

### Los Script .py se encuentran estructurados de manera que se ejecuten como cuaderno Jupiter pero desde el VSCODE para llevar un mejor seguimiento y mostrar el paso a paso de la ejecución del PROCESO.

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

### Tener presente que las librerias que se utilizan en colab o entornos ONLINE a veces no son compatibles con las que se ejecutan en VSCODE
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlostrujillo-academy/Proyecto_ETL_Fuga_de_Cerebros/blob/main/Notebook/main.ipynb)`main.ipynb`
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlostrujillo-academy/Proyecto_ETL_Fuga_de_Cerebros/blob/main/Notebook/Scrapean_Computrabajo.ipynb) `scraper_salarios.ipynb`
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/carlostrujillo-academy/Proyecto_ETL_Fuga_de_Cerebros/blob/main/Notebook/Coordenadas_munici.ipynb) `geolocalizacion.ipynb`

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
