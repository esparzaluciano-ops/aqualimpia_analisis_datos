import pandas as pd
import matplotlib.pyplot as plt

# 1. Carga de datos
# Lee el archivo CSV y lo convierte en un DataFrame [cite: 715]
df = pd.read_csv("dataset_set_A_aguas_residuales.csv")

# Convertir la fecha a tipo datetime para correcto ordenamiento temporal [cite: 750]
df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")

# 2. Archivo para el Área de Operaciones
# Exportación de reporte centrado en métricas de ejecución [cite: 401, 513]
df_operaciones = df[[
    "fecha_registro", "planta", "caudal_entrada_m3_d", 
    "DBO_entrada_mg_L", "DBO_salida_mg_L", "energia_aeracion_kWh", "lodos_generados_kg_d"
]]
df_operaciones.to_excel("reporte_operaciones.xlsx", index=False)

# 3. Archivo para el Área de Gestión Ambiental
# Exportación de reporte centrado en indicadores de cumplimiento [cite: 401, 513]
df_ambiental = df[[
    "fecha_registro", "planta", "DBO_salida_mg_L", "cumplimiento_norma"
]]
df_ambiental.to_excel("reporte_ambiental.xlsx", index=False)

# 4. Construcción del Dashboard Exploratorio
# Agrupación de métricas promedio por planta para análisis comparativo [cite: 426]
resumen_plantas = df.groupby("planta")[["caudal_entrada_m3_d", "DBO_salida_mg_L"]].mean()

plt.figure(figsize=(12, 5))

# Gráfico 1: Caudal de entrada promedio por planta
plt.subplot(1, 2, 1)
plt.bar(resumen_plantas.index, resumen_plantas["caudal_entrada_m3_d"], color='skyblue')
plt.title("Caudal de Entrada Promedio por Planta")
plt.ylabel("Caudal (m3/d)")

# Gráfico 2: DBO de salida promedio por planta
plt.subplot(1, 2, 2)
plt.bar(resumen_plantas.index, resumen_plantas["DBO_salida_mg_L"], color='salmon')
plt.title("DBO de Salida Promedio por Planta")
plt.ylabel("DBO Salida (mg/L)")

plt.tight_layout()
plt.show()