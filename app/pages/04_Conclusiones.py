import streamlit as st

st.set_page_config(
    page_title="Conclusiones",
    page_icon="✅",
    layout="wide"
)

st.title("Conclusiones finales")

st.markdown("""
En esta sección se resumen los principales hallazgos del proyecto, las limitaciones del análisis
y posibles próximos pasos para continuar el trabajo.
""")

st.markdown("---")

st.header("Hallazgos principales")

st.markdown("""
A partir del proceso de inspección, limpieza, análisis exploratorio y PCA, se observaron los siguientes resultados:

- El dataset original presentaba problemas de calidad, como duplicados, valores faltantes, categorías inconsistentes, fechas problemáticas y valores numéricos fuera de rango.
- La etapa de limpieza permitió generar una versión más consistente del dataset sin modificar el archivo original.
- El tiempo mensual de visualización fue una variable central para analizar el comportamiento de los usuarios.
- Los usuarios del plan Premium presentaron mayores niveles de visualización promedio que los usuarios de los planes Básico y Estándar.
- Las diferencias de visualización promedio por país fueron menos marcadas.
- El análisis conjunto entre género favorito, plan y tiempo de visualización mostró que el plan de suscripción parece tener una relación más clara con el consumo que el género favorito.
- El PCA permitió visualizar la información numérica en componentes principales, aunque no mostró una separación clara entre los usuarios según el plan de suscripción.
""")

st.markdown("---")

st.header("Limitaciones del análisis")

st.markdown("""
El análisis realizado presenta algunas limitaciones:

- El dataset tenía problemas de calidad que requirieron decisiones de limpieza e imputación.
- Algunas fechas de último inicio de sesión eran inválidas, faltantes o futuras, por lo que fueron marcadas como no válidas.
- El análisis es exploratorio, por lo tanto no permite afirmar causalidad.
- Aunque los usuarios Premium presentan mayor consumo promedio, no se puede afirmar que el plan cause directamente ese mayor consumo.
- PCA se aplicó únicamente sobre variables numéricas seleccionadas.
- Variables categóricas como país, género favorito y plan de suscripción no fueron incluidas directamente en PCA.
""")

st.markdown("---")

st.header("Próximos pasos")

st.markdown("""
Como posibles mejoras o continuaciones del proyecto, se podrían considerar:

- Incorporar nuevas variables del comportamiento de los usuarios, como antigüedad de la cuenta, cantidad de sesiones o dispositivos utilizados.
- Analizar la evolución temporal del consumo si se contara con datos históricos.
- Profundizar el análisis por segmentos de usuarios.
- Comparar patrones de consumo entre países con mayor detalle.
- Evaluar otras técnicas de reducción de dimensionalidad o segmentación en futuros trabajos.
- Mejorar la aplicación interactiva incorporando filtros para explorar el dataset de forma más dinámica.
""")

st.markdown("---")

st.header("Cierre")

st.markdown("""
El proyecto permitió aplicar un flujo completo de minería de datos: inspección inicial, preparación de datos,
análisis exploratorio, reducción de dimensionalidad y comunicación de resultados.

El proceso permitió transformar un dataset con problemas de calidad en una base más consistente para el análisis,
manteniendo trazabilidad de las decisiones mediante notebooks y un log ETL.
""")

st.success("El proyecto queda documentado mediante notebooks, README, log ETL, informe final y aplicación Streamlit.")
