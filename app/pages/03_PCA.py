import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(
    page_title="PCA",
    page_icon="📉",
    layout="wide"
)

# Ruta raíz del proyecto
ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "processed" / "streaming_users_clean.csv"

@st.cache_data
def cargar_dataset():
    return pd.read_csv(DATA_PATH, parse_dates=["last_login_date"])

df = cargar_dataset()

st.title("Reducción de dimensionalidad con PCA")

st.markdown("""
En esta sección se aplica Análisis de Componentes Principales (PCA) sobre variables numéricas del dataset limpio.

El objetivo es analizar si la información numérica puede representarse en menos dimensiones y observar si los usuarios se agrupan según el plan de suscripción.
""")

st.markdown("---")

st.header("Variables utilizadas")

variables_pca = [
    "age",
    "monthly_watch_time_mins",
    "customer_support_tickets"
]

st.markdown("""
Para aplicar PCA se seleccionaron variables numéricas del dataset:

- `age`
- `monthly_watch_time_mins`
- `customer_support_tickets`

No se incluyó `user_id`, ya que es un identificador y no una variable útil para el análisis de componentes principales.
""")

X = df[variables_pca]

st.dataframe(X.head(10), use_container_width=True)

st.markdown("---")

st.header("Escalamiento aplicado")

st.markdown("""
Antes de aplicar PCA se utilizó `StandardScaler`.

Este paso es necesario porque las variables tienen escalas diferentes. Por ejemplo, la edad tiene valores mucho menores que el tiempo mensual de visualización.

El escalamiento evita que una variable domine el análisis solo por tener valores numéricos más grandes.
""")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

st.markdown("---")

st.header("Aplicación de PCA")

pca = PCA()
X_pca = pca.fit_transform(X_scaled)

varianza_explicada = pca.explained_variance_ratio_

varianza_pca = pd.DataFrame({
    "Componente": [f"PC{i+1}" for i in range(len(varianza_explicada))],
    "Varianza explicada (%)": (varianza_explicada * 100).round(2),
    "Varianza acumulada (%)": (varianza_explicada.cumsum() * 100).round(2)
})

st.subheader("Tabla de varianza explicada")

st.dataframe(varianza_pca, use_container_width=True)

st.markdown("""
La tabla muestra qué porcentaje de la variabilidad total explica cada componente principal.

En este dataset, las tres componentes explican porcentajes similares de varianza. Esto indica que la información numérica está distribuida de manera pareja entre las variables utilizadas.
""")

st.markdown("---")

# =========================
# Visualización 1
# =========================

st.header("1. Varianza explicada por componentes")

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(
    varianza_pca["Componente"],
    varianza_pca["Varianza explicada (%)"],
    label="Varianza explicada"
)

ax.plot(
    varianza_pca["Componente"],
    varianza_pca["Varianza acumulada (%)"],
    marker="o",
    label="Varianza acumulada"
)

ax.set_title("Varianza explicada por componentes principales")
ax.set_xlabel("Componentes principales")
ax.set_ylabel("Porcentaje de varianza")
ax.legend()

st.pyplot(fig)

st.markdown("""
**Interpretación:**  
El gráfico muestra que ninguna componente concentra por sí sola la mayor parte de la información.

PC1 y PC2 juntas permiten visualizar los datos en dos dimensiones, pero no conservan la totalidad de la variabilidad original. Por eso, en este caso PCA es útil principalmente como herramienta de exploración y visualización.
""")

st.markdown("---")

# =========================
# Visualización 2
# =========================

st.header("2. Proyección PCA: PC1 vs PC2")

pca_df = pd.DataFrame(
    X_pca[:, :2],
    columns=["PC1", "PC2"]
)

pca_df["subscription_plan"] = df["subscription_plan"].values

fig, ax = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=pca_df,
    x="PC1",
    y="PC2",
    hue="subscription_plan",
    alpha=0.6,
    ax=ax
)

ax.set_title("Proyección PCA: PC1 vs PC2 según plan de suscripción")
ax.set_xlabel("Componente principal 1")
ax.set_ylabel("Componente principal 2")
ax.legend(title="Plan de suscripción")

st.pyplot(fig)

st.markdown("""
**Interpretación:**  
El gráfico muestra a los usuarios proyectados sobre las dos primeras componentes principales.

Los colores correspondientes a los planes Básico, Estándar y Premium aparecen bastante mezclados. Esto indica que las variables numéricas utilizadas en PCA no separan claramente a los usuarios según el plan de suscripción.
""")

st.markdown("---")

st.header("Loadings")

loadings = pd.DataFrame(
    pca.components_.T,
    index=variables_pca,
    columns=[f"PC{i+1}" for i in range(len(variables_pca))]
)

st.dataframe(loadings.round(3), use_container_width=True)

st.markdown("""
Los loadings permiten interpretar qué variables originales tienen mayor peso en cada componente principal.

En este análisis, PC1 está más influenciada por `age` y `customer_support_tickets`, mientras que PC2 está más relacionada con `monthly_watch_time_mins`.
""")

st.success("Esta sección incluye 2 visualizaciones, respetando el máximo solicitado para PCA.")
