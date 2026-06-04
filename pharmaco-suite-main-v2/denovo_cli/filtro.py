import pandas as pd
import os

# 1. Definir las rutas de los archivos
ruta_lbp = "resultados-lbp/candidates_admet.csv"
ruta_sbp = "resultados-sbp/candidates_admet.csv"
ruta_rbp = "resultados-rbp/candidates_admet.csv"
ruta_consensus = "resultados-consensus/candidates_admet.csv"

# 2. Cargar las tablas CSV en DataFrames
# Asumimos que los archivos están separados por comas (por defecto en read_csv)
df_lbp = pd.read_csv(ruta_lbp)
df_sbp = pd.read_csv(ruta_sbp)
df_rbp = pd.read_csv(ruta_rbp)
df_consensus = pd.read_csv(ruta_consensus)

# NOTA: En Python, la primera columna es el índice 0, la segunda es el índice 1.
# Usamos .iloc[:, 1] para seleccionar todas las filas (:) de la segunda columna (1).

# 3. Extraer los códigos SMILES de sbp, rbp y consensus y convertirlos a "sets" (conjuntos)
# Los conjuntos son muy rápidos para buscar intersecciones
smiles_sbp = set(df_sbp.iloc[:, 1])
smiles_rbp = set(df_rbp.iloc[:, 1])
smiles_consensus = set(df_consensus.iloc[:, 1])

# 4. Encontrar los SMILES que están presentes en LAS TRES tablas adicionales
smiles_comunes = smiles_sbp.intersection(smiles_rbp).intersection(smiles_consensus)

# 5. Filtrar la tabla "template" (resultados-lbp)
# Mantenemos solo las filas donde el valor de la segunda columna esté dentro de 'smiles_comunes'
df_final = df_lbp[df_lbp.iloc[:, 1].isin(smiles_comunes)]

# 6. Guardar el resultado en la carpeta actual
archivo_salida = "candidates_admet.csv"
df_final.to_csv(archivo_salida, index=False)

# Mostrar un resumen al terminar
print(f"Búsqueda finalizada.")
print(f"Fármacos originales en resultados-lbp: {len(df_lbp)}")
print(f"Fármacos en común en las 4 carpetas: {len(df_final)}")
print(f"El archivo filtrado se ha guardado exitosamente como: {archivo_salida}")
