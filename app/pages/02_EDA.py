import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(
    page_title="EDA",
    page_icon="📊",
    layout="wide"
)

# Ruta raíz del proyecto
ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "processed" / "streaming_users_clean.csv"

@st.cache_data
def cargar_dataset():
    return pd.read_csv(DATA_PATH, parse_dates=["last_login_date"])

df = cargar_dataset()

st.title("Análisis exploratorio de datos")

st.markdown("""
En esta sección se presentan las cinco visualizaciones principales del análisis exploratorio.

El objetivo es analizar la distribución de los usuarios y estudiar el comportamiento del tiempo mensual de visualización según distintas variables del dataset.
""")

st.markdown("---")

# =========================
# 1. Univariada categórica
# =========================

st.header("1. Usuarios por plan de suscripción")

fig, ax = plt.subplots(figsize=(8, 5))

sns.countplot(
    data=df,
    x="subscription_plan",
    order=df["subscription_plan"].value_counts().index,
    ax=ax
)

ax.set_title("Cantidad de usuarios por plan de suscripción")
ax.set_xlabel("Plan de suscripción")
ax.set_ylabel("Cantidad de usuarios")

st.pyplot(fig)

st.markdown("""
**Interpretación:**  
Este gráfico permite observar cómo se distribuyen los usuarios entre los distintos planes de suscripción.

La visualización ayuda a identificar qué planes concentran mayor cantidad de usuarios dentro del dataset.
""")

st.markdown("---")

# =========================
# 2. Univariada numérica
# =========================

st.header("2. Distribución del tiempo mensual de visualización")

fig, ax = plt.subplots(figsize=(8, 5))

sns.histplot(
    data=df,
    x="monthly_watch_time_mins",
    bins=30,
    kde=True,
    ax=ax
)

ax.set_title("Distribución del tiempo mensual de visualización")
ax.set_xlabel("Tiempo mensual de visualización (minutos)")
ax.set_ylabel("Cantidad de usuarios")

st.pyplot(fig)

st.markdown("""
**Interpretación:**  
La distribución muestra que la mayoría de los usuarios se concentra en valores moderados de tiempo mensual de visualización.

También se observa una cola hacia la derecha, lo que indica la presencia de un grupo menor de usuarios con consumos más altos.
""")

st.markdown("---")

# =========================
# 3. Bivariada
# =========================

st.header("3. Tiempo mensual de visualización según plan")

fig, ax = plt.subplots(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="subscription_plan",
    y="monthly_watch_time_mins",
    ax=ax
)

ax.set_title("Tiempo mensual de visualización según plan de suscripción")
ax.set_xlabel("Plan de suscripción")
ax.set_ylabel("Tiempo mensual de visualización (minutos)")

st.pyplot(fig)

st.markdown("""
**Interpretación:**  
El boxplot permite comparar la distribución del tiempo mensual de visualización entre los planes de suscripción.

Se observa que los usuarios del plan Premium presentan valores centrales más altos, mientras que el plan Básico muestra menores niveles de consumo.
""")

st.markdown("---")

# =========================
# 4. Bivariada
# =========================

st.header("4. Promedio de visualización mensual por país")

promedio_pais = (
    df.groupby("country")["monthly_watch_time_mins"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig, ax = plt.subplots(figsize=(9, 5))

sns.barplot(
    data=promedio_pais,
    x="country",
    y="monthly_watch_time_mins",
    ax=ax
)

ax.set_title("Promedio de tiempo mensual de visualización por país")
ax.set_xlabel("País")
ax.set_ylabel("Promedio de visualización mensual (minutos)")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)

st.markdown("""
**Interpretación:**  
Este gráfico compara el promedio de tiempo mensual de visualización entre países.

Los promedios resultan bastante similares entre las regiones analizadas, por lo que no se observan diferencias fuertes en el consumo promedio según país.
""")

st.markdown("---")

# =========================
# 5. Multivariada
# =========================

st.header("5. Promedio de visualización por género favorito y plan")

tabla_genero_plan = df.pivot_table(
    values="monthly_watch_time_mins",
    index="favorite_genre",
    columns="subscription_plan",
    aggfunc="mean"
)

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(
    tabla_genero_plan,
    annot=True,
    fmt=".0f",
    cmap="Blues",
    ax=ax
)

ax.set_title("Promedio de visualización por género favorito y plan")
ax.set_xlabel("Plan de suscripción")
ax.set_ylabel("Género favorito")

st.pyplot(fig)

st.markdown("""
**Interpretación:**  
El heatmap permite analizar de manera conjunta el género favorito, el plan de suscripción y el tiempo mensual de visualización.

Se observa que los usuarios Premium presentan mayores promedios de visualización en casi todos los géneros. Además, las diferencias entre planes parecen más marcadas que las diferencias entre géneros dentro de un mismo plan.
""")

st.markdown("---")

st.success("Esta sección incluye exactamente 5 visualizaciones: 2 univariadas, 2 bivariadas y 1 multivariada.")
