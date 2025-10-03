import pandas as pd

# Ruta relativa dentro del repo
csv_path = "data/import/migracion.zip"

# Leer el CSV directamente desde el ZIP
df = pd.read_csv(csv_path, compression="zip", sep=";", encoding="latin1")

print(df.shape)
print(df.head())
