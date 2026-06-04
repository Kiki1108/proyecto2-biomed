import pandas as pd

# 1. Definir las rutas de los archivos
ruta_lbp = "resultados-lbp/candidates_admet.csv"
ruta_sbp = "resultados-sbp/candidates_admet.csv"
ruta_rbp = "resultados-rbp/candidates_admet.csv"
ruta_consensus = "resultados-consensus/candidates_admet.csv"

# 2. Cargar las tablas CSV en DataFrames
df_lbp = pd.read_csv(ruta_lbp)
df_sbp = pd.read_csv(ruta_sbp)
df_rbp = pd.read_csv(ruta_rbp)
df_consensus = pd.read_csv(ruta_consensus)

# 3. Extraer los códigos SMILES a conjuntos (sets) para una búsqueda ultra rápida
smiles_sbp = set(df_sbp.iloc[:, 1])
smiles_rbp = set(df_rbp.iloc[:, 1])
smiles_consensus = set(df_consensus.iloc[:, 1])

# 4. Función para contar en cuántas de las otras 3 tablas aparece el SMILES
def en_cuantas_tablas_adicionales_esta(smiles):
    contador = 0
    if smiles in smiles_sbp: 
        contador += 1
    if smiles in smiles_rbp: 
        contador += 1
    if smiles in smiles_consensus: 
        contador += 1
    return contador

# 5. Aplicamos la función a la segunda columna del template (resultados-lbp)
# Buscamos los que sumen >= 2 (Es decir: 1 de lbp + al menos 2 de las otras = 3 o más en total)
presencia_adicional = df_lbp.iloc[:, 1].apply(en_cuantas_tablas_adicionales_esta)

# Filtramos la tabla original manteniendo solo las filas que cumplen la condición
df_final = df_lbp[presencia_adicional >= 1]

# 6. Guardar el resultado en la carpeta actual
archivo_salida = "candidates_admet.csv"
df_final.to_csv(archivo_salida, index=False)

# Mostrar un resumen al terminar
print(f"Búsqueda finalizada con la regla: 'Presente en lbp y en al menos otras 2 tablas'")
print(f"Fármacos originales en resultados-lbp: {len(df_lbp)}")
print(f"Fármacos que cumplen la condición: {len(df_final)}")
print(f"El archivo filtrado se ha guardado exitosamente como: {archivo_salida}")
