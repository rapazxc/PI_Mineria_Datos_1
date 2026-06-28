# Informe final - Proyecto Integrador Minería de Datos I

## 1. Contexto y objetivo

Este proyecto analiza un dataset de usuarios de una plataforma de streaming. El objetivo fue aplicar un proceso completo de minería de datos, incluyendo inspección inicial, preparación de datos, análisis exploratorio, reducción de dimensionalidad y comunicación de resultados.

El análisis se centró en estudiar la calidad de los datos y explorar patrones relacionados con el tiempo mensual de visualización de los usuarios.

## 2. Dataset y calidad de datos

El dataset contiene información de usuarios, incluyendo edad, plan de suscripción, país, género favorito, tiempo mensual de visualización, fecha de último inicio de sesión y tickets de soporte.

Durante la inspección inicial se detectaron problemas de calidad como duplicados completos, `user_id` repetidos, valores faltantes, categorías inconsistentes, fechas inválidas o futuras y valores numéricos fuera de rango.

El dataset original fue conservado sin modificaciones en `data/raw`. Luego se generó una versión procesada en `data/processed`, manteniendo trazabilidad mediante el archivo `logs/pipeline_log.csv`.

## 3. Preparación de datos

La limpieza incluyó la eliminación de duplicados completos, normalización de categorías, tratamiento de valores numéricos inválidos, conversión y validación de fechas, y consolidación de registros repetidos por `user_id`.

Las decisiones fueron tomadas a partir de evidencia observada en la inspección inicial y documentadas en los notebooks del proyecto.

## 4. Análisis exploratorio

El análisis exploratorio se centró principalmente en el tiempo mensual de visualización.

Se observó que la mayoría de los usuarios presenta consumos moderados, con una cola hacia valores altos. Al comparar por plan de suscripción, los usuarios Premium presentaron mayores niveles de visualización promedio que los usuarios de planes Básico y Estándar.

El análisis por país mostró diferencias menos marcadas, con promedios relativamente similares entre regiones. El análisis conjunto entre género favorito, plan y tiempo de visualización mostró que las diferencias entre planes fueron más claras que las diferencias entre géneros.

## 5. PCA

Se aplicó PCA sobre las variables numéricas `age`, `monthly_watch_time_mins` y `customer_support_tickets`.

Antes de aplicar PCA se utilizó `StandardScaler`, ya que las variables tenían escalas diferentes.

Los resultados mostraron que la varianza se distribuyó de manera similar entre las tres componentes principales. La proyección en PC1 y PC2 permitió visualizar los datos, pero no mostró una separación clara entre los usuarios según el plan de suscripción.

## 6. Conclusiones y limitaciones

El proyecto permitió transformar un dataset con problemas de calidad en una base más consistente para el análisis.

El principal patrón observado fue que el tiempo mensual de visualización varía especialmente según el plan de suscripción, con mayores valores promedio en usuarios Premium.

El análisis es exploratorio, por lo que no permite afirmar causalidad. Además, PCA se aplicó solo sobre variables numéricas seleccionadas y no incluyó directamente variables categóricas como país, género favorito o plan.

## 7. Enlaces

Repositorio GitHub: [pendiente]  
Aplicación Streamlit: [pendiente]  
README: `README.md`  
Log ETL: `logs/pipeline_log.csv`
