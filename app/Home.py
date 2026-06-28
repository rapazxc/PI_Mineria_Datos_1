import streamlit as st

st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos I",
    page_icon="📊",
    layout="wide"
)

st.title("Proyecto Integrador - Minería de Datos I")

st.subheader("Análisis de usuarios de una plataforma de streaming")

st.markdown("""
Este proyecto analiza un dataset de usuarios de una plataforma de streaming mediante un proceso de minería de datos.

El trabajo incluye inspección inicial, preparación y calidad de datos, análisis exploratorio, reducción de dimensionalidad con PCA y comunicación de resultados mediante una aplicación interactiva.
""")

st.markdown("---")

st.header("Información del proyecto")

st.markdown("""
**Materia:** Minería de Datos I  
**Integrantes:** [Completar integrantes]  
**Comisión:** [Completar comisión]  
**Fecha:** Junio 2026  
""")

st.markdown("---")

st.header("Objetivo general")

st.markdown("""
Aplicar un proceso de minería de datos sobre un dataset de usuarios de streaming, identificando problemas de calidad, preparando una versión limpia, explorando patrones de comportamiento y aplicando PCA sobre variables numéricas.
""")

st.markdown("---")

st.header("Enlaces")

st.markdown("""
- **Repositorio GitHub:** [Ver repositorio](https://github.com/rapazxc/PI_Mineria_Datos_1)
- **Aplicación Streamlit:** [Abrir aplicación](https://pimineriadatos1-tqsw3bdv3lqgxtqkwaqpti.streamlit.app/)
- **Informe final:** `reports/informe_final.pdf`
- **Log ETL:** `logs/pipeline_log.csv`
""")

st.info("La aplicación comunica los principales resultados para público general. La evidencia técnica completa se encuentra en los notebooks del repositorio.")
