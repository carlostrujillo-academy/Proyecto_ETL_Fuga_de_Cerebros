
#%% Geolocalización de ciudades colombianas
import pandas as pd
from geopy.geocoders import Nominatim
import time
#%%
# === CONFIGURACIÓN ===
# Nombre del archivo de entrada
archivo_entrada = "validacion_municipios.xlsx"
# Nombre del archivo de salida
archivo_salida = "Ciudades_colombianas_con_coordenadas.xlsx"
# Nombre de la hoja que contiene los datos
hoja = "ciudades_paises"

# === CARGAR DATOS ===
df = pd.read_excel(archivo_entrada, sheet_name=hoja)

# Inicializar geocodificador
geolocator = Nominatim(user_agent="ciudades_colombia_locator")

def obtener_coordenadas(ciudad, departamento):
    """Busca coordenadas de una ciudad en Colombia"""
    try:
        location = geolocator.geocode(f"{ciudad}, {departamento}, Colombia", timeout=15)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Error con {ciudad}, {departamento}: {e}")
        return None, None
    return None, None

# Crear nuevas columnas
df["Latitud"] = None
df["Longitud"] = None

# === PROCESO DE GEOCODIFICACIÓN ===
for i, row in df.iterrows():
    ciudad = row["Ciudad_Origen"]
    depto = row["Departamento/Estado.1"]

    lat, lon = obtener_coordenadas(ciudad, depto)
    df.at[i, "Latitud"] = lat
    df.at[i, "Longitud"] = lon

    print(f"{i+1}/{len(df)} - {ciudad}, {depto} -> {lat}, {lon}")
    
    time.sleep(1.5)  # pausa para no saturar el servidor

# === GUARDAR RESULTADOS ===
df.to_excel(archivo_salida, index=False)
print(f"Archivo generado: {archivo_salida}")

# %%
    