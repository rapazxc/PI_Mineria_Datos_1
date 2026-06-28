import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Dataset",
    page_icon="📁",
    layout="wide"
)

# Ruta raíz del proyecto
ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = ROOT / "data" / "processed" / "streaming_users_clean.csv"
LOG_PATH = ROOT / "logs" / "pipeline_log.csv"

@st.cache_data
def cargar_dataset():
    return pd.read_csv(DATA_PATH, parse_dates=["last_login_date"])

@st.cache_data
def cargar_log():
    if LOG_PATH.exists():
        return pd.read_csv(LOG_PATH)
    return None

df = cargar_dataset()
log_etl = cargar_log()

st.title("Dataset")

st.markdown("""
En esta sección se presenta el dataset utilizado en el proyecto, junto con un resumen general de su estructura,
su calidad y las principales transformaciones realizadas durante la etapa de preparación.
""")

st.markdown("---")

st.header("Descripción general")

st.markdown("""
El dataset contiene información de usuarios de una plataforma de streaming.

Cada registro representa un usuario y contiene variables relacionadas con edad, plan de suscripción,
país, género favorito, tiempo mensual de visualización, fecha de último inicio de sesión y tickets de soporte.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Filas", df.shape[0])

with col2:
    st.metric("Columnas", df.shape[1])

with col3:
    st.metric("Valores faltantes", int(df.isnull().sum().sum()))

st.markdown("---")

st.header("Vista previa del dataset limpio")

st.dataframe(df.head(20), use_container_width=True)

st.markdown("""
La tabla anterior muestra una vista previa de la versión procesada del dataset, ubicada en `data/processed`.

El archivo original se conserva sin modificaciones en `data/raw`.
""")

st.markdown("---")

st.header("Variables del dataset")

variables = pd.DataFrame({
    "Variable": df.columns,
    "Tipo de dato": df.dtypes.astype(str),
    "Valores faltantes": df.isnull().sum().values
})

st.dataframe(variables, use_container_width=True)

st.markdown("---")

st.header("Resumen breve de calidad")

st.markdown("""
Durante la inspección inicial se detectaron problemas de calidad en el dataset, entre ellos:

- Registros duplicados completos.
- `user_id` repetidos.
- Valores faltantes.
- Categorías escritas de distintas formas.
- Fechas inválidas o futuras.
- Valores numéricos fuera de rango.

Estas situaciones fueron revisadas y tratadas en el notebook `02_calidad_y_limpieza.ipynb`.
""")

st.markdown("---")

st.header("Transformaciones principales")

st.markdown("""
Las principales acciones realizadas fueron:

- Eliminación de duplicados completos.
- Normalización de categorías en variables como plan, país y género favorito.
- Tratamiento de valores inválidos en variables numéricas.
- Conversión y validación de fechas.
- Consolidación de registros repetidos por `user_id`.
- Generación de una versión limpia del dataset en `data/processed`.
""")

st.markdown("---")

st.header("Log ETL")

if log_etl is not None:
    st.markdown("""
    El siguiente log resume las transformaciones realizadas durante la preparación de los datos.
    """)
    st.dataframe(log_etl, use_container_width=True)
else:
    st.warning("No se encontró el archivo `logs/pipeline_log.csv`.")
